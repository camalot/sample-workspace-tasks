param(
    # [switch] — present or absent; $true when the flag is passed, $false otherwise
    [switch]$Verbose,

    [switch]$DryRun,

    [switch]$NoCache
)

Write-Host "Verbose:  $Verbose"
Write-Host "Dry run:  $DryRun"
Write-Host "No cache: $NoCache"

if ($DryRun) {
    Write-Host "[DRY RUN] No changes were made."
}
if ($Verbose) {
    Write-Host "[VERBOSE] Detailed output enabled."
}
if ($NoCache) {
    Write-Host "[INFO] Cache is disabled."
}
