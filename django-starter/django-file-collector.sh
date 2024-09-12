#!/bin/bash

# Directorio de destino para los archivos recopilados
OUTPUT_DIR="claude_project_files"

# Crear el directorio de salida
mkdir -p "$OUTPUT_DIR"

# Función para copiar y renombrar archivos
copy_and_rename() {
    local src="$1"
    local dst="$2"
    local app_name="$3"
    
    if [ -f "$src" ]; then
        cp "$src" "$dst"
        echo "Copiado: $src -> $dst"
    fi
}

# Copiar archivos principales del proyecto
copy_and_rename "manage.py" "$OUTPUT_DIR/manage.py"
copy_and_rename "requirements.txt" "$OUTPUT_DIR/requirements.txt"

# Encontrar el directorio del proyecto Django (asumiendo que está en el directorio actual)
PROJECT_DIR=$(find . -maxdepth 1 -type d -name "*" ! -name ".*" ! -name "__pycache__" -print -quit)

if [ -d "$PROJECT_DIR" ]; then
    # Copiar archivos principales del proyecto
    copy_and_rename "$PROJECT_DIR/settings.py" "$OUTPUT_DIR/project_settings.py"
    copy_and_rename "$PROJECT_DIR/urls.py" "$OUTPUT_DIR/project_urls.py"

    # Encontrar y procesar todas las aplicaciones
    find . -type d -name "migrations" | while read -r app_dir; do
        app_dir=$(dirname "$app_dir")
        app_name=$(basename "$app_dir")
        
        # Copiar y renombrar archivos de la aplicación
        copy_and_rename "$app_dir/models.py" "$OUTPUT_DIR/${app_name}_models.py" "$app_name"
        copy_and_rename "$app_dir/views.py" "$OUTPUT_DIR/${app_name}_views.py" "$app_name"
        copy_and_rename "$app_dir/urls.py" "$OUTPUT_DIR/${app_name}_urls.py" "$app_name"
        copy_and_rename "$app_dir/forms.py" "$OUTPUT_DIR/${app_name}_forms.py" "$app_name"
        copy_and_rename "$app_dir/admin.py" "$OUTPUT_DIR/${app_name}_admin.py" "$app_name"
    done
else
    echo "No se pudo encontrar el directorio del proyecto Django."
fi

echo "Proceso completado. Los archivos se han copiado en el directorio $OUTPUT_DIR"
