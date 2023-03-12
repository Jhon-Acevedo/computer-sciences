const modalParameters = document.getElementById("linearCongruence")

modalParameters.addEventListener("click", () => {$("#myModalB").modal('show');});

const exportGraph = document.getElementById("export")

function saveData() {
    alert("Exporting graph to PNG");
}

exportGraph.addEventListener("click", () => { saveData(); });