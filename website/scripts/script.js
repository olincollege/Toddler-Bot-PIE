makeNav();

function makeNav() {
    const nav = document.querySelector("nav");
    
    const titles = ["Home", "Mechanical", "Electrical", "Software", "Budget", "BOM"];
    const pages = ["./index.html", "./mechanical.html", "./electrical.html", "./software.html", "./budget.html", "./bom.html"];

    for (let i = 0; i < titles.length; i++) {
        const anchor = document.createElement("a");
        anchor.innerHTML = titles[i];
        anchor.href = pages[i];
        nav.appendChild(anchor);
    }
}