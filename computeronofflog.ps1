Get-WinEvent -FilterHashtable @{LogName='System'; ID=6005,6006,6008,41} | Select-Object TimeCreated, Id, Message | Sort-Object TimeCreated
