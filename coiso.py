import logging
from logging.handlers import RotatingFileHandler

# Configuração básica do logging
logging.basicConfig(level=logging.INFO)

# Criando um logger específico para auditoria
audit_logger = logging.getLogger('audit')
audit_logger.setLevel(logging.INFO)

# Definindo um manipulador para gravar os logs em um arquivo com rotação (limite de 5MB por arquivo)
handler = RotatingFileHandler('audit.log', maxBytes=5*1024*1024, backupCount=5)
handler.setLevel(logging.INFO)

# Formato de log personalizado para auditoria
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Adicionando o manipulador ao logger
audit_logger.addHandler(handler)

# Exemplo de log de auditoria
audit_logger.info('Usuário admin realizou login')
audit_logger.warning('Tentativa de login falhada para o usuário guest')
audit_logger.error('Erro ao acessar o banco de dados para o usuário admin')