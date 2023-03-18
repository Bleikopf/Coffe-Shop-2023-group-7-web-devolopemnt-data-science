const FIGURE = $("#figure");
const NAME = 'Coffe-Shop-2023-group-7-web-devolopemnt-data-science/'

function loadMap(name) {
    FIGURE.load(`../${name}maps/${name}.html`);
}

loadMap('25sqm2emp');
