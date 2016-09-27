echo "sprd_log_debug version 0.1 usage"
echo "sprd_debug_log record task/log/irq info"
echo "crash> struct sched_log -o sprd_debug_log"
echo "struct sched_log {"
echo  "[c0929380] struct task_log task[4][1024];"
echo  "[c0949380] struct irq_log irq[4][1024];"
echo  "[c0961380] struct work_log work[4][1024];"
#echo "[c0979380] struct hrtimer_log hrtimers[4][8];"
echo "}"
echo "saved the log named task/irq/work_log and run this sh"
echo "crash> struct task_log c0929380 -c 4096 > task_log"
echo "crash> struct irq_log c0949380 -c 4096 > irq_log"
echo "crash> struct work_log c0961380 -c 4096 > work_log"
#echo "crash> struct hrtimer_log c0979380 -c 32 > hrtimer_log"

echo "starting .................................."
#echo task
sed ':a;N;$!ba;s/\n/ /g' task_log  | sed "s/}  struct /\n/g"  | sed "s/^.*time = //g" > task
sed -n '1,   1024p' task | sed 's/$/&,\tcpu0 /g' > task.0
sed -n '1025,2048p' task | sed 's/$/&,\tcpu1 /g' > task.1
sed -n '2049,3072p' task | sed 's/$/&,\tcpu2 /g' > task.2
sed -n '3073,4096p' task | sed 's/$/&,\tcpu3 /g' > task.3
cat task.* >> task_all
sort -g task_all > task_all_sort

#echo irq
sed ':a;N;$!ba;s/\n/ /g' irq_log   | sed "s/}  struct /\n/g"  | sed "s/^.*time = //g" > irq
sed -n '1,   1024p' irq | sed 's/$/&,\tcpu0 /g' > irq.0
sed -n '1025,2048p' irq | sed 's/$/&,\tcpu1 /g' > irq.1
sed -n '2049,3072p' irq | sed 's/$/&,\tcpu2 /g' > irq.2
sed -n '3073,4096p' irq | sed 's/$/&,\tcpu3 /g' > irq.3
cat irq.* >> irq_all
sort -g irq_all > irq_all_sort

#echo work
sed ':a;N;$!ba;s/\n/ /g' work_log  | sed "s/}  struct /\n/g"  | sed "s/^.*time = //g" >  work
sed -n '1,   1024p' work | sed 's/$/&,\tcpu0 /g' > work.0
sed -n '1025,2048p' work | sed 's/$/&,\tcpu1 /g' > work.1
sed -n '2049,3072p' work | sed 's/$/&,\tcpu2 /g' > work.2
sed -n '3073,4096p' work | sed 's/$/&,\tcpu3 /g' > work.3
cat work.* >> work_all
sort -g work_all > work_all_sort

#echo all
cat *_all_sort >> sprd_log
sort -g sprd_log > sprd_log_sort 

echo recently 10 work by cat work_all_sort
cat work_all_sort | tail -n 10

echo recently 10 irqs by cat irq_all_sort
cat irq_all_sort | grep "en = 1"| tail -n 10

echo recently 10 task by cat task_all_sort
cat task_all_sort | tail -n 10 

echo recently 20 by cat sprd_log_sort  
cat sprd_log_sort | tail -n 20

#echo mkdir
mkdir sprd_debug_log 
mkdir sprd_debug_log/task 
mkdir sprd_debug_log/irq
mkdir sprd_debug_log/work

#move
mv task* sprd_debug_log/task/ 
mv irq* sprd_debug_log/irq/
mv work* sprd_debug_log/work/
cp sprd_debug_log/task/task_log .
cp sprd_debug_log/irq/irq_log .
cp sprd_debug_log/work/work_log .
mv sprd_log sprd_debug_log
cp sprd_log_sort sprd_debug_log
