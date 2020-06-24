
## 删除大文件
$> big_file_name

## 批量删除小文件, test是空目录，cache-bak是要清空的目录
$rsync --delete-before -a -H  --stats test/ cache-bak/
