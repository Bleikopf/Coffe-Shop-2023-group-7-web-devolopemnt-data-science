const FIGURE = $("#figure");

function loadMap(name) {
    FIGURE.load(`../maps/${name}.html`);
}

loadMap('plotly');