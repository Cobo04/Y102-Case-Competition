let Data = "";
let hasData = false;

function getData() {
    
    url = "/api/datapoint";

    axios.get(url)
    .then(function(response) {

        // The data will all be returned as a JSON object
        // We can access the data by using the data property of the response object

        document.getElementById('randomNumberDiv').innerHTML = response.data;
        document.getElementById('discover').innerHTML = "Check in!";
        Data = response.data;

    })
    .catch(function(error) {
        console.log(error);
    });
}

function submitData() {
    document.getElementById('randomNumberDiv').innerHTML = "";
    document.getElementById('discover').innerHTML = "Please Scan Code!";
    Data = "";
    hasData = true;
}

window.addEventListener("load", (event) => {
    var intervalID = window.setInterval(getData, 500);
});