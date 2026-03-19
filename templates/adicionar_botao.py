"""
SCRIPT: Adicionar botão "Editar este Template" em todos os templates finais.

COMO USAR:
1. Coloque este arquivo na MESMA pasta onde estão seus Templates (Template1.py, Template2.py, etc.)
2. Execute: python adicionar_botao.py
3. Pronto! Todos os arquivos serão atualizados automaticamente.
"""

import os
import ast

EDIT_BTN_TEMPLATE = '''
    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template{NUM}" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)
'''

# Mapeamento: nome do arquivo → número do template
FILE_MAP = {
    "Template1.py":  1,  "Template2.py":  2,  "Template3.py":  3,
    "Template4.py":  4,  "Template5.py":  5,  "Template6.py":  6,
    "Template7.py":  7,  "Template8.py":  8,  "Template9.py":  9,
    "Template10.py": 10, "Template11.py": 11, "Template12.py": 12,
    "Template13.py": 13, "Template14.py": 14, "Template15.py": 15,
    "Template16.py": 16, "Template17.py": 17, "Template18.py": 18,
    "Template19.py": 19, "Template20.py": 20, "Template21.py": 21,
    "Template22.py": 22, "Template23.py": 23, "Template24.py": 24,
    "Template25.py": 25, "Template26.py": 26, "Template27.py": 27,
    "Template28.py": 28, "Template29.py": 29, "Template30.py": 30,
    "Template31.py": 31, "Template32.py": 32, "Template33.py": 33,
    "Template34.py": 34, "Template35.py": 35,
}

def add_button(src: str, num: int) -> str:
    """Adiciona o botão no final da função render(), antes de qualquer código fora dela."""
    
    # Se já tem o botão, não duplica
    if 'sttackedit.streamlit.app' in src:
        return src
    
    btn = EDIT_BTN_TEMPLATE.replace('{NUM}', str(num))
    
    # Tenta inserir antes dos marcadores comuns de fim de arquivo
    markers = [
        '\nif __name__',
        '\n# Execução',
        '\n# ========== FIM',
        '\n# Lembre-se:',
    ]
    for marker in markers:
        if marker in src:
            return src.replace(marker, btn + marker, 1)
    
    # Se não encontrar marcador, adiciona no final
    return src.rstrip() + '\n' + btn + '\n'

def validate_syntax(src: str, filename: str) -> bool:
    """Verifica se o Python está sintaticamente correto."""
    try:
        ast.parse(src)
        return True
    except SyntaxError as e:
        print(f"    ⚠️  Erro de sintaxe em {filename}: {e}")
        return False

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("  ADICIONAR BOTÃO EDITAR — STTACK SITE")
    print("=" * 60)
    print(f"\nPasta: {current_dir}\n")
    
    processed = 0
    skipped   = 0
    errors    = 0
    
    for filename, num in FILE_MAP.items():
        filepath = os.path.join(current_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"  ⬜ {filename} — não encontrado, pulando")
            skipped += 1
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        if 'sttackedit.streamlit.app' in original:
            print(f"  ✅ {filename} — botão já existe, pulando")
            skipped += 1
            continue
        
        modified = add_button(original, num)
        
        if not validate_syntax(modified, filename):
            print(f"  ❌ {filename} — erro de sintaxe após modificação, revertendo")
            errors += 1
            continue
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        
        print(f"  ✅ {filename} — botão adicionado → template{num}")
        processed += 1
    
    print("\n" + "=" * 60)
    print(f"  CONCLUÍDO: {processed} atualizados | {skipped} pulados | {errors} erros")
    print("=" * 60)

if __name__ == "__main__":
    main()
