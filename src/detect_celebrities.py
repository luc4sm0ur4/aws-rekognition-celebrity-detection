import boto3
import argparse

def detect_celebrities(image_path):
    client = boto3.client('rekognition')
    
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()
    
    response = client.recognize_celebrities(Image={'Bytes': image_bytes})
    
    celebs = []
    for celeb in response['CelebrityFaces']:
        celebs.append({
            "Nome": celeb['Name'],
            "Confiança": f"{celeb['MatchConfidence']:.2f}%",
            "Posição": celeb['Face']['BoundingBox']
        })
    
    return celebs

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', required=True, help='Caminho da imagem (ex: img/foto_evento.jpg)')
    args = parser.parse_args()
    
    celebridades = detect_celebrities(args.image)
    
    if celebridades:
        print("🎬 Celebridades Detectadas:")
        for idx, celeb in enumerate(celebridades, 1):
            print(f"\n{idx}. Nome: {celeb['Nome']}")
            print(f"   Confiança: {celeb['Confiança']}")
            print(f"   Posição na Imagem: {celeb['Posição']}")
    else:
        print("Nenhuma celebridade detectada.")
