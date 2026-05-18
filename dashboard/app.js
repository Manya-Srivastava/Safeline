// app.js

document.getElementById('gasForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent form submission to avoid page reload

    // Get values from the input fields
    const co = document.getElementById('co').value;
    const ch4 = document.getElementById('ch4').value;
    const h2s = document.getElementById('h2s').value;
    const o2 = document.getElementById('o2').value;

    // Validate inputs (ensure all are filled and valid numbers)
    if (!co || !ch4 || !h2s || !o2 || isNaN(co) || isNaN(ch4) || isNaN(h2s) || isNaN(o2)) {
        alert('Please enter valid numeric values for all fields.');
        return;
    }

    // Prepare the data to send to Flask API
    const data = { 
        CO: parseFloat(co), 
        CH4: parseFloat(ch4), 
        H2S: parseFloat(h2s), 
        O2: parseFloat(o2) 
    };

    // Send data to the Flask API
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response from server:", data);
        const riskOutput = document.getElementById('riskLevel');
    
        if (data.risk_level) {
            riskOutput.innerText = "Risk Level: " + data.risk_level;
            riskOutput.style.color = data.risk_level === "High" ? "red" : (data.risk_level === "Medium" ? "orange" : "green");
        } else if (data.error) {
            riskOutput.innerText = "Error: " + data.details;
            riskOutput.style.color = "red";
        } else {
            riskOutput.innerText = "Unexpected response from server.";
            riskOutput.style.color = "gray";
        }
    })
    
    .catch(error => {
        console.error('Error:', error);
        alert("Error occurred while predicting the risk level.");
    });
});
