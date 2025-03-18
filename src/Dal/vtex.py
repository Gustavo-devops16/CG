import requests
import time

def collect_products(seller_id):

    base_url = "https://compresuapeca.vtexcommercestable.com.br/api/catalog_system/pub/products/search"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-VTEX-API-AppKey": "vtexappkey-compresuapeca-EXFYRB",
        "X-VTEX-API-AppToken": "YTTDSLNTAADIGUNPOZYGNASSJZLWDTNNWPJNNTDLNUXVOAFQPKPVILGPBRCTQYHQOIWOVQOKCYFPKQXGPPVBTTXBKEVKKHBKZDIDKLIJMUWTEEBQRSAFFIUYAIQCBKFS"
    }


    _from = 0
    _to = 49
    total_coletado = 0
    tamanho_pagina = 50  

    collected_products = []

    
    while True:
        url = f"{base_url}?_from={_from}&_to={_to}&fq=sellerId:{seller_id}" 
        
        try:
            response = requests.get(url, headers=headers)
            
            
            if response.status_code == 200 or response.status_code == 206:
                products = response.json()
            
                if not products:
                    print("Não há mais produtos para coletar.")
                    break
            
                for product in products:
                    product_id = product.get("productId", "N/A")
                    product_name = product.get("productName", "N/A")
                    description = product.get("description", "N/A")
                    brand_id = product.get("brandId", "N/A")
                    category_id = product.get("categoryId", "N/A")
                    productRef = (product.get("productReference", "N/A"))
                    
                    seller_ids = []

                    items = product.get("items", [])
                    for item in items:
                        sellers = item.get("sellers", [])
                        
                        for seller in sellers:
                            seller_id = seller.get("sellerId", "N/A")
                            seller_ids.append(seller_id)
                    
                    # Junta todos os sellerId em uma string separada por vírgula
                    seller_id_str = ", ".join(seller_ids) if seller_ids else "N/A"
                    
                    # Adiciona as informações dos produtos na lista
                    collected_products.append({
                        "productId": product_id,
                        "productName": product_name,
                        "description": description,
                        "BrandId": brand_id,
                        "categoryId": category_id,
                        "sellerId": seller_id_str,
                        "productReference": productRef
                    })
                
                # Mostra o progresso da coleta
                total_coletado += len(products)
                print(f"Coletados até agora: {total_coletado} produtos")
                
                # Se retornou menos que o tamanho da página, não há mais produtos
                if len(products) < tamanho_pagina:
                    print("Última página alcançada.")
                    break
                
                # Atualiza os parâmetros para a próxima página
                _from += tamanho_pagina
                _to += tamanho_pagina
                
                # Pausa para evitar sobrecarregar a API
                time.sleep(1)
            
            else:
                print(f"Erro na requisição: {response.status_code}")
                break

        except requests.exceptions.RequestException as e:
            print(f"Ocorreu um erro na requisição: {e}")
            break

    return collected_products