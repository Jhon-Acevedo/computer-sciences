const graph = document.getElementById("graph")

graph.addEventListener("click", () => {
    const xi = graph.getAttribute('value').substring(0, 1);
    const yi = graph.getAttribute('value').substring(2, 3)
    createGraphicNormal(xi, yi);
    const iterations = data.length;
    const interval = [];
    if (iterations < 1000) {
        createInterval(interval, 10);
        createGraphicNormal(xi, yi, interval);
    } else {
        createInterval(interval, 40)
        createGraphicNormal(xi, yi, interval);
    }
});

function createGraphicNormal(xi, yi, interval) {
    try {
        const numberIntervals = interval.length - 1;
        const mydata = calculateFrequency(numberIntervals);
        const ejeX = [];
        mydata.forEach((value) => {
            ejeX.push(value.toString());
        });
        $("#myModalG").modal('show');
        const ctx = document.getElementById('myChart');
        const name = exportFile.getAttribute("name");
        new Chart(ctx, {
            type: 'bar', label: name + ' Distribution', data: {
                labels: interval, datasets: [{
                    label: name + ' Distribution', data: ejeX, borderWidth: 1
                }]
            }, options: {
                plugins: {
                    zoom: {
                        modifierKey: 'shift', pan: {
                            enabled: true,
                        }
                    }
                }, scales: {
                    y: {
                        title: {
                            text: "Frequency",
                            display: true
                        },
                        beginAtZero: true
                    },
                    x: {
                        title: {
                            text: "Intervals",
                            display: true
                        },
                    }
                }
            }
        });
    } catch (e) {
        showAlertError();
    }
}

function createInterval(interval, iterations) {
    for (let i = 0; i < iterations + 1; i++)
        interval.push(i);
}

function calculateFrequency(numberIntervals) {
    const values = data.map(({0: yi, 2: xi}) => ({yi, xi}))
    const max = Math.max.apply(Math, values.map(function (o) {
        return o.xi;
    }));
    const min = Math.min.apply(Math, values.map(function (o) {
        return o.xi;
    }));
    const range = max - min;
    const interval = range / numberIntervals;
    const frequency = [];
    for (let i = 0; i < numberIntervals; i++) {
        frequency.push(0);
    }
    values.forEach(({xi}) => {
        const index = Math.floor((xi - min) / interval);
        frequency[index]++;
    });
    return frequency;
}

