param(
    # [string[]] — accepts one or more string values as an array
    # Usage: -Tags backend,api,v2  or  -Tags backend -Tags api
    [Parameter(Mandatory=$false)]
    [string[]]$Tags,

    # Required string array — one or more input file paths
    [Parameter(Mandatory=$true)]
    [string[]]$Files,

    # int array — exactly the values provided
    [Parameter(Mandatory=$false)]
    [int[]]$Ports = @(8080, 8443)
)

Write-Host "Tags:  $($Tags -join ', ')"
Write-Host "Files: $($Files -join ', ')"
Write-Host "Ports: $($Ports -join ', ')"

foreach ($file in $Files) {
    Write-Host "  Processing: $file"
}
