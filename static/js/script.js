async function analyzeComplaint() {

    const complaint =
        document.getElementById("complaint").value;

    const resultDiv =
        document.getElementById("result");

    if (!complaint.trim()) {

        alert("Please enter complaint");

        return;
    }

    resultDiv.innerHTML = `
        <div class="loading">
            Analyzing cyber complaint...
        </div>
    `;

    try {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                complaint: complaint
            })
        });

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        let severityClass = "low";

        if (data.severity === "Medium") {
            severityClass = "medium";
        }

        if (data.severity === "High") {
            severityClass = "high";
        }

        if (data.severity === "Critical") {
            severityClass = "critical";
        }

        resultDiv.innerHTML = `

            <div class="card">

                <h2>Threat Analysis Result</h2>

                <div class="severity ${severityClass}">
                    ${data.severity} Threat
                </div>

                <p>
                    <strong>Scam Category:</strong>
                    ${data.category}
                </p>

                <p>
                    <strong>Applicable Laws:</strong>
                    ${data.laws.join(", ")}
                </p>

                <h3>Extracted Evidence</h3>

                <div class="evidence-grid">

                    <div class="evidence-card">
                        <h4>Phone Numbers</h4>
                        <p>${data.extracted_data.phones.join("<br>") || "None"}</p>
                    </div>

                    <div class="evidence-card">
                        <h4>Emails</h4>
                        <p>${data.extracted_data.emails.join("<br>") || "None"}</p>
                    </div>

                    <div class="evidence-card">
                        <h4>URLs</h4>
                        <p>${data.extracted_data.urls.join("<br>") || "None"}</p>
                    </div>

                    <div class="evidence-card">
                        <h4>Amounts</h4>
                        <p>${data.extracted_data.amounts.join("<br>") || "None"}</p>
                    </div>

                    <div class="evidence-card">
                        <h4>UPI IDs</h4>
                        <p>${data.extracted_data.upi_ids.join("<br>") || "None"}</p>
                    </div>

                </div>

                <h3>Safety Recommendations</h3>

                <ul>
                    ${data.safety_tips.map(
                        tip => `<li>${tip}</li>`
                    ).join("")}
                </ul>

                <h3>Police Report Summary</h3>

                <div class="summary-box">
                    <pre>${data.summary}</pre>
                </div>

                <button onclick="downloadReport()">
                    Download Report
                </button>

            </div>
        `;

        window.currentReport = data.summary;

    } catch (error) {

        resultDiv.innerHTML = `
            <div class="error">
                Error: ${error.message}
            </div>
        `;
    }
}

function downloadReport() {

    const blob = new Blob(
        [window.currentReport],
        { type: "text/plain" }
    );

    const a = document.createElement("a");

    a.href = URL.createObjectURL(blob);

    a.download = "cyber_report.txt";

    a.click();
}