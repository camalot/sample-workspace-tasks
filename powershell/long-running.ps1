# Long running PowerShell script

Write-Host "Starting long running PowerShell script..." -ForegroundColor Yellow
for ($i = 1; $i -le 10; $i++) {
    Write-Host "Progress: $i/10"
    Start-Sleep -Seconds 1
}
Write-Host "Long running script completed!" -ForegroundColor Green
