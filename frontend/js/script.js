const FIGURE = $("#figure");

// ONLOAD TEST
Plotly.newPlot( FIGURE[0], [{
	x: [1, 2, 3, 4, 5],
	y: [1, 2, 4, 8, 16] }], {
	margin: { t: 0 } } );


function loadMap(name) {
    FIGURE.load(`../maps/${name}.html`);
}