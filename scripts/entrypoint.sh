<<<<<<< HEAD
#!/bin/sh

echo "case $1"

case "$1" in

  'elk')
  	ARGS=""
  	exec twint $@ $ARGS
	;;

  'tor')
  	# ARGS="-ip `hostname -i` -dir /data"
  	# if [ -n "$MASTER_PORT_9333_TCP_ADDR" ] ; then
	#	ARGS="$ARGS -master.peers=$MASTER_PORT_9333_TCP_ADDR:$MASTER_PORT_9333_TCP_PORT"
	# fi
  	exec twint $@ $ARGS
  	;;

  'ui')
  	ARGS=""
  	exec twint $@ $ARGS
	;;

  'sh')
  	exec /bin/sh $@
	;;

  'cronjob')
	# MASTER=${WEED_MASTER-localhost:9333}
	# FIX_REPLICATION_CRON_SCHEDULE=${CRON_SCHEDULE-*/7 * * * * *}
	# echo "$FIX_REPLICATION_CRON_SCHEDULE" 'echo "volume.fix.replication" | weed shell -master='$MASTER > /crontab
	# BALANCING_CRON_SCHEDULE=${CRON_SCHEDULE-25 * * * * *}
	# echo "$BALANCING_CRON_SCHEDULE" 'echo "volume.balance -c ALL -f" | weed shell -master='$MASTER >> /crontab
	echo "Running Crontab:"
	cat /crontab
	exec supercronic /crontab
	;;
  *)
	apk add --no-cache nano bash
  	exec bash
	;;
esac
=======
#!/bin/bash
$@
>>>>>>> 8bba455a67283c8e3f19524b32f35fa831184811
