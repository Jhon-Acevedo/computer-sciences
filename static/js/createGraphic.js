const graph = document.getElementById("graph")
graph.addEventListener("click", () => {
    const xi = graph.getAttribute('value').substring(0, 1);
    const yi = graph.getAttribute('value').substring(2, 3)
    createGraphic(xi, yi);
});

function createGraphic(xi, yi) {
    try {
        const values = data.map(({0: yi, 2: xi}) => ({yi, xi}))
        const max = Math.max.apply(Math, values.map(function (o) {
            return o.xi;
        }));
        const min = Math.min.apply(Math, values.map(function (o) {
            return o.xi;
        }));

        $("#myModalG").modal('show');
        const ctx = document.getElementById('myChart');
        const name = exportFile.getAttribute("name");
        new Chart(ctx, {
            type: 'line',
            label: name + ' Distribution',
            data: {
                labels: values.map(({yi}) => yi),
                datasets: [{
                    label: name + ' Distribution',
                    data: values.map(({xi}) => xi),
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    zoom: {
                        modifierKey: 'shift',
                        pan: {
                            enabled: true,
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (e) {
        showAlertError();
    }
}