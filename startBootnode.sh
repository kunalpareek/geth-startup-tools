echo "Generating boot key"
bootnode -genkey boot.key
echo "Starting bootnode"
nohup bootnode -nodekey boot.key &
echo "Bootnode started"
cat nohup.out
exit