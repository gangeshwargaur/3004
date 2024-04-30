try:
    f = open(filename)

except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: % d', e.errno)


# ==================================================================
    try:
        client_obj.get_url(url)
    except (URLError, ValueError, SocketTimeout):
        client_obj.remove_url(url)