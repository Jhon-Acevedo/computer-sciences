$(document).ready(function () {
  $('#alertParameter').hide();
});

function showAlertError() {
  $('#alertParameter').css('visibility', 'visible');
  $('#alertParameter').fadeTo(2000, 500).slideUp(500, function () {
      $('#alertParameter').slideUp(500);
  });
}

console.log("std normal distribution.js")

const modalParameters = document.getElementById("stdNormalDistribution")

modalParameters.addEventListener("click", () => {$("#myModalB").modal('show');});


const exportFile = document.getElementById("export")
exportFile.addEventListener("click", () => {
    try {
        const values = data.map(({5: ri}) => ({ri}))
        const csvContent = "data:text/csv;charset=utf-8," + values.map(e => e.ri).join("\n");
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "std_normal_dist.csv");
        document.body.appendChild(link);
        link.click();
    } catch (e) {
        showAlertError();
    }
});

//mostar la grafica
const graph = document.getElementById("graph")
graph.addEventListener("click", () => {
    try {
        const values = data.map(({0: yi, 2: xi}) => ({yi, xi}))
        $("#myModalG").modal('show');
        const ctx = document.getElementById('myChart');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: values.map(({yi}) => yi),
                datasets: [{
                    label: 'Linear Congruence',
                    data: values.map(({xi}) => xi),
                    borderWidth: 1
                }]
            },
            options: {
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
});