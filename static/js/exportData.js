const exportFile = document.getElementById("export");
exportFile.addEventListener("click", () => {
        saveCSV(exportFile.getAttribute("name"), exportFile.getAttribute("value"));
    }
);

function saveCSV(name, colum) {
    try {
        const column = colum.valueOf();
        const values = data.map((e) => ({ri: e[column]}));
        const csvContent = "data:text/csv;charset=utf-8," + values.map((e) => e.ri).join("\n");
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", `${name}.csv`);
        document.body.appendChild(link);
        link.click();
    } catch (e) {
        showAlertError();
    }
}