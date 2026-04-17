# Read blog.html
$blog_path = "d:\网站开发-json\pages\blog.html"
$content = Get-Content -Path $blog_path -Raw -Encoding UTF8

# Find article patterns
$articles = [regex]::Matches($content, '<article id="(ai-daily-\d+[a-z]?)"')
Write-Host "Found $($articles.Count) articles"
$articles[0..9] | ForEach-Object { Write-Host $_.Value.Substring(0, [Math]::Min(50, $_.Value.Length)) }

# Check the structure of existing article
$firstArticle = [regex]::Match($content, '<article id="ai-daily-20260416b".*?</article>', [System.Text.RegularExpressions.RegexOptions]::Singleline)
if ($firstArticle.Success) {
    Write-Host "`nFirst article preview (first 2000 chars):"
    Write-Host $firstArticle.Value.Substring(0, [Math]::Min(2000, $firstArticle.Value.Length))
}
