async function fetchData() {
    const logContainer = document.getElementById('dataLog');
    
    try {
        // Adjust the URL if your API is running on a different port
        const response = await fetch('http://127.0.0.1:5010/sales/cities');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Clear log and display raw JSON for verification
        logContainer.innerHTML = '';
        data.forEach(item => {
            const entry = document.createElement('div');
            entry.className = 'log-entry';
            entry.textContent = JSON.stringify(item);
            logContainer.appendChild(entry);
        });

        // Initialize Chart
        renderChart(data);

    } catch (error) {
        logContainer.innerHTML = `<span style="color: #ff5555;">Error: ${error.message}</span><br>Make sure your FastAPI server is running and CORS is enabled.`;
        console.error('Fetch error:', error);
    }
}

function renderChart(data) {
    const ctx = document.getElementById('cityChart').getContext('2d');
    
    // Sort data by revenue for better visualization
    const sortedData = data.sort((a, b) => b.total_revenue - a.total_revenue).slice(0, 10);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sortedData.map(item => item.city),
            datasets: [{
                label: 'Total Revenue ($)',
                data: sortedData.map(item => item.total_revenue),
                backgroundColor: 'rgba(52, 152, 219, 0.7)',
                borderColor: 'rgba(41, 128, 185, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
}

// Start fetching when the page loads
window.onload = fetchData;
