const graph = document.getElementById("graph")
graph.addEventListener("click", () => {
    const xi = graph.getAttribute('value').substring(0, 1);
    const yi = graph.getAttribute('value').substring(2, 3)
    createGraphic(2, 0);
});

function createGraphic(xi, yi) {
    try {
        const values = data.map((e) => ({yi: e[yi], xi: e[xi]}));
        $("#myModalG").modal('show');
        const ctx = document.getElementById('myChart');
        new Chart(ctx, {
            type: 'line', data: {
                labels: values.map(({yi}) => yi), datasets: [{
                    label: 'Normal Distribution', data: values.map(({xi}) => xi), borderWidth: 1
                }]
            }, options: {
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