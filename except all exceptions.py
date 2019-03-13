# just for example
try:
    process(record)
    if changed:
        update(record)
except (KeyboardInterrupt, SystemExit):
    rollback()
    raise
except Exception as e:
    logger.exception(e)
    rollback()
    # report error and proceed
else:
    commit()