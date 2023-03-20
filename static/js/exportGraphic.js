const exportGraph = document.getElementById("exportG");

exportGraph.addEventListener("click", () => {
    const name = exportFile.getAttribute("name")
    const imageLink = document.createElement("a");
    const canvas = document.getElementById("myChart");
    imageLink.download = `${name}.jpg`;
    imageLink.href = canvas.toDataURL("image/jpg", 1).replace("image/jpg", "image/octet-stream")
    imageLink.click();
});