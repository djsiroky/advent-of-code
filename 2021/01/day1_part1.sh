if [ $# -ne 1 ]; then
  echo 1>&2 "$0: Need 1 argument only"
  exit 2
fi

count=0
PREV=-1
cat $1 | while read line; do
  if (( $PREV == -1 )); then
    echo "${line:0:-1} (N/A - No previous measurement)"
  elif (( ${line:0:-1} > $PREV )); then
    ((count+=1))
    echo "${line:0:-1} (increased)"
  else
    echo "${line:0:-1} (decreased)"
  fi
  PREV=${line:0:-1}
  echo "Number of increases: $count"
done