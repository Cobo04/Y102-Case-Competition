function getData() {
    
    url = "/api/datapoint";

    axios.get(url)
    .then(function(response) {

        // The data will all be returned as a JSON object
        // We can access the data by using the data property of the response object

        document.getElementById('randomNumberDiv').innerHTML = response.data;
    })
    .catch(function(error) {
        console.log(error);
    });
}

window.addEventListener("load", (event) => {
    var intervalID = window.setInterval(getData, 500);
});