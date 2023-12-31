<?php
$reportFolder = 'reports';

// Get all HTML files in the reports folder
$files = glob("$reportFolder/*.html");

// Sort files by modification time, newest first
usort($files, function($a, $b) {
    return filemtime($b) - filemtime($a);
});

?>
<html>
<head>
    <title>Test Reports</title>
</head>
<body>
    <h1>Test Reports</h1>
    <ul>
        <?php foreach ($files as $file): ?>
            <?php
                $fileName = basename($file);
                $fileDate = date('Y-m-d H:i:s', filemtime($file));
            ?>
            <li><a href="<?php echo $file; ?>"><?php echo $fileName; ?></a> - <?php echo $fileDate; ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
