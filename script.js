
function submitReview() {
    const review = document.getElementById("reviewInput").value;
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ review: review })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
    });
}
