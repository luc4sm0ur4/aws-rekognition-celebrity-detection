# Detectando Celebridades em Imagens com AWS Rekognition

![AWS Rekognition](img/aws-rekognition-logo.png)  
*Identificação de celebridades em imagens usando inteligência artificial da AWS.*

## 📝 Visão Geral
Este projeto utiliza o **AWS Rekognition** para detectar celebridades em imagens, retornando seus nomes e informações de localização (caixas delimitadoras). Ideal para análise de mídia, curadoria de conteúdo e aplicações de entretenimento.

## 🛠 Pré-requisitos
- Conta na AWS ([criar aqui](https://aws.amazon.com/pt/)).
- AWS CLI instalado ([guia](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)).
- Python 3.8+ e biblioteca Boto3 (`pip install boto3`).
- Uma imagem com possíveis celebridades (ex: `foto_evento.jpg`).

## 🔑 Configuração da AWS
1. **Crie um usuário IAM**:
   - Acesse o **Console AWS > IAM**.
   - Crie um usuário com permissão `AmazonRekognitionFullAccess`.
   - Gere as **Access Key ID** e **Secret Access Key**.

2. **Configure a AWS CLI**:
   ```bash
   aws configure
