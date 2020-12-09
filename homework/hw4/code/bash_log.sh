for filepath in ./*.log; do
  BASENAME=$(basename $filepath)
  FILE_RESULT="${BASENAME%.*}.out"
  wc -l < "$filepath" > "$FILE_RESULT"
  printf "\n" >> "$FILE_RESULT"
  awk -F ' ' '{print substr($6, 2)}' "$filepath" | sort | uniq -c >> "$FILE_RESULT"
  printf "\n" >> "$FILE_RESULT"
  sort -k10 -n -r "$filepath" | awk -F ' ' '{print $7" "$9" "$10}' | head -10 >> "$FILE_RESULT"
  printf "\n" >> "$FILE_RESULT"
  awk '{ if ($9~/4[[:digit:]]{2}/) print $7" "$9" "$1}' "$filepath" | sort -n -k3 | uniq -c | sort -rn -k1 | head -10 >> "$FILE_RESULT"
  printf "\n" >> "$FILE_RESULT"
  awk '{ if ($9~/5[[:digit:]]{2}/) print $7" "$9" "$1" "$10}' "$filepath" | sort -nr -k4 | head -10 >> "$FILE_RESULT"
done



