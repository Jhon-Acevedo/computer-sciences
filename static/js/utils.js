// Para validar que ingreso parametros
$(document).ready(function () {
  $("#alertParameter").hide();
});

function showAlertError() {
  $("#alertParameter").css("visibility", "visible");
  $("#alertParameter")
    .fadeTo(2000, 500)
    .slideUp(500, function () {
      $("#alertParameter").slideUp(500);
    });
}

// Para mostrar los datos en la tabla
showParameters("Multiplicativa");

function showParameters(element) {
  console.log(element);
  const modalParameters = document.getElementById(element);
  modalParameters.addEventListener("click", () => {
    $("#myModalB").modal("show");
  });
}

// Exportat los datos en un archivo csv
const exportFile = document.getElementById("export");
exportFile.addEventListener("click", () => {
  try {
    const values = data.map(({ 5: ri }) => ({ ri }));
    const csvContent =
      "data:text/csv;charset=utf-8," + values.map((e) => e.ri).join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "multiplicativeCongruence.csv");
    document.body.appendChild(link);
    link.click();
  } catch (e) {
    showAlertError();
  }
});


