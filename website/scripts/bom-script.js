const grid = document.querySelector(".grid");
loadBOM(grid);

async function loadBOM(grid) {
    // load csv
    const response = await fetch("https://raw.githubusercontent.com/olincollege/Toddler-Bot-PIE/refs/heads/main/website/data/bom.csv",
        {
            method: "GET",
            mode: "cors"
        }
    );
    const text = await response.text();
    const lines = text.trim().split('\n')

    // add cells
    for (let i = 1; i < lines.length; i++) {
        const row = lines[i].split(',');
        // add non-link cells
        for (let j = 0; j < row.length-4; j++) {
            const cell = document.createElement("span");
            cell.classList.add("grid-item");
            cell.innerHTML = row[j];
            grid.appendChild(cell);
        }
        
        // add cells with links
        for (let j = row.length-4; j < row.length-1; j += 2) {
            const cell = document.createElement("a");
            cell.classList.add("grid-item")
            cell.innerHTML = row[j];
            if (row[j] !== "n/a")
                cell.href = row[j+1];
            grid.appendChild(cell);
        }
    }
}