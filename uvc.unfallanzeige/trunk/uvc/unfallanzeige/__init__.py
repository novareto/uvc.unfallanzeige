import logging
from zope.i18nmessageid import MessageFactory

logger = logging.getLogger('uvc.unfallanzeige')

UvcUnfallanzeigeMessageFactory = MessageFactory('uvc.unfallanzeige')

def log(message, summary='', severity=logging.INFO):
    logger.log(severity, '%s %s', summary, message)
