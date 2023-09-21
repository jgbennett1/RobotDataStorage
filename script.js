document.addEventListener("DOMContentLoaded", function () {
    const sendPostButton = document.getElementById("sendPostButton");

    sendPostButton.addEventListener("click", function () {
        // Create a data object to send in the POST request
        const data = {
            key1: "value1",
            key2: "value2"
            // Add more key-value pairs as needed
        };

        // Convert the data object to JSON
        const jsonData = JSON.stringify(data);
        //console.log(jsonData);

        // Send the POST request to the specified URL
        fetch('http://localhost:5502/', {
           method: 'POST',
           body: `{"UserID":${new Date().getTime()},"OperationData":[`,
           headers: {
               'Content-Type': 'application/json'
           },
           mode: "no-cors"
       });
       /*
       .then(response => response.json())
       .then(data => {
           console.log(data.message);
       })
       .catch(error => {
           console.error('Error:', error);
       });
       */
    });
});
