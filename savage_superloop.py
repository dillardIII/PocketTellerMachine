<!DOCTYPE html>
<html>
<head>
    <title>Savage Emperor Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
<h1>💀 Savage Emperor Dashboard</h1>
<canvas id="walletChart" width="400" height="200"></canvas>
<canvas id="vaultChart" width="400" height="200"></canvas>
<script>
async function loadWalletChart() {
    const res = await fetch('/wallets');
    const data = await res.json();
    const ctx = document.getElementById('walletChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map((v,i)=>i),
            datasets: [{
                label: 'Wallet Finds',
                data: data.map(d=>Math.random()*100),
                borderColor: 'red'
            }]
        }
    });
}
async function loadVaultChart() {
    const res = await fetch('/vault');
    const data = await res.json();
    const ctx = document.getElementById('vaultChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map((v,i)=>i),
            datasets: [{
                label: 'Vault Events',
                data: data.map(d=>Math.random()*100),
                borderColor: 'blue'
            }]
        }
    });
}
loadWalletChart(); loadVaultChart();
</script>
</body>
</html>