const FIGURE = $("#figure");
const GITROOT = 'Coffe-Shop-2023-group-7-web-devolopemnt-data-science/'

function loadMap(name) {
    FIGURE.load(`../${GITROOT}maps/${name}.html`);
}

loadMap('25sqm2emp');
