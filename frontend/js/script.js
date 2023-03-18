const FIGURE = $("#figure");

function loadMap(name) {
    FIGURE.load(`../tree/maps/${name}.html`);
}

loadMap('25sqm2emp');
