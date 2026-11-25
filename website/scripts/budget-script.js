const grid = document.querySelector(".grid");
loadBOM(grid);

async function loadBOM(grid) {
    // load csv
    const response = await fetch("https://raw.githubusercontent.com/olincollege/Toddler-Bot-PIE/refs/heads/main/website/data/budget.csv",
        {
            method: "GET",
            mode: "cors"
        }
    );
    const text = await response.text();
    const lines = text.trim().split('\n')

    // add cells
    for (let i = 1; i < lines.length-1; i++) {
        const row = lines[i].split(',');
        // add non-link cells
        for (let j = 0; j < row.length-2; j++) {
            const cell = document.createElement("span");
            cell.classList.add("grid-item");
            cell.innerHTML = row[j];
            grid.appendChild(cell);
        }
        
        // add cells with links
        const cell = document.createElement("a");
        cell.classList.add("grid-item")
        cell.innerHTML = row[row.length-2];
        if (row[row.length-2] !== "n/a")
            cell.href = row[row.length-1];
        grid.appendChild(cell);
    }

    // write total
    const total = lines[lines.length-1].split(',')[3];
    document.getElementById("total").innerHTML = `Total spent: ${total}`;
}