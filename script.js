async function checkFact() {
    const claimInput = document.getElementById('claimInput').value;
    const resultDiv = document.getElementById('result');

    if (!claimInput) {
        resultDiv.innerHTML = '<div class="alert alert-danger">Please enter a claim to fact-check.</div>';
        return;
    }

    resultDiv.innerHTML = '<div class="alert alert-info">Checking fact... Please wait.</div>';

    try {
        const response = await axios.post('http://127.0.0.1:5000/check-fact', {
            claim: claimInput
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        let resultHTML = '<h3>Fact-Checking Results:</h3>';
        for (const [fact, check] of Object.entries(response.data)) {
            resultHTML += `
                <div class="card mb-3">
                    <div class="card-body">
                        <h5 class="card-title">${fact}</h5>
                        <p class="card-text">${check}</p>
                    </div>
                </div>
            `;
        }

        resultDiv.innerHTML = resultHTML;
    } catch (error) {
        console.error(error);
        resultDiv.innerHTML = '<div class="alert alert-danger">An error occurred while checking the fact. Please try again.</div>';
    }
}