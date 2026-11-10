# Source - https://stackoverflow.com/a/69314205
# Posted by Gulbu, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-03, License - CC BY-SA 4.0
import pygame

from svg.path import parse_path, Move
from xml.dom import minidom

from pathlib import Path

def get_point_at(path, distance, scale, offset):
    pos = path.point(distance)
    pos += offset
    pos *= scale
    return pos.real, pos.imag


def points_from_path(path, density, scale, offset):
    step = max(2, int(path.length() * density))
    int(path.length() * density)
    last_step = step - 1

    if last_step == 0:
        yield get_point_at(path, 0, scale, offset)
        return

    for distance in range(step):
        yield get_point_at(
            path, distance / last_step, scale, offset)


def points_from_doc(doc, density=5, scale=1, offset=0):
    offset = offset[0] + offset[1] * 1j
    strokes = []
    for element in doc.getElementsByTagName("path"):
        current_stroke = []
        for segment in parse_path(element.getAttribute("d")):
            if isinstance(segment, Move):
            # save the previous stroke and start a new one
                if current_stroke:
                    strokes.append(current_stroke)
                    current_stroke = []
            else:
                # these points continue the current stroke
                current_stroke.extend(points_from_path(segment, density, scale, offset))
        if current_stroke:
            strokes.append(current_stroke)
    return strokes


string = Path(r"c:/Users/maria/Downloads/Toddler-Bot-PIE/scanning/add-circle-svgrepo-com.svg").read_text(encoding="utf-8")

doc = minidom.parseString(string)
points = points_from_doc(doc, density=1, scale=5, offset=(0, 5))
doc.unlink()

def order_of_points(points):
    pass


def main():
    screen = pygame.display.set_mode([500, 500])
    screen.fill((255, 255, 255))

    doc = minidom.parseString(string)
    strokes = points_from_doc(doc, density=5, scale=5, offset=(0, 5))
    doc.unlink()

    for i, stroke in enumerate(strokes):
        color = pygame.Color(0, 0, 0)
        color.hsva = (360 * i / len(strokes), 100, 80, 100)
        for point in stroke:
            pygame.draw.circle(screen, color, point, 1)

    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


pygame.init()
main()
pygame.quit()
