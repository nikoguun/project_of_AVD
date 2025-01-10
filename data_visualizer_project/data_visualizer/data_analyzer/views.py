from django.shortcuts import render, redirect
from .forms import CSVUploadForm
import csv
from io import TextIOWrapper
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns 
from django.contrib import messages


# Fonction pour traiter le fichier CSV
def handle_uploaded_file(f):
    file = TextIOWrapper(f, encoding='utf-8')
    csv_reader = csv.reader(file)
    data = list(csv_reader)
    return data

def home(request):
    return render(request, 'data_analyzer/home.html', {
        'features': {
            'upload': 'Téléchargez vos fichiers CSV',
            'analyze': 'Analysez vos données',
            'visualize': 'Créez des visualisations interactives'
        }
    })

# Vue pour uploader un fichier CSV
def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        form = CSVUploadForm(request.POST, request.FILES)
        messages.success(request, 'Fichier téléchargé avec succès!')
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data = handle_uploaded_file(csv_file)
            # Stocker les données dans la session pour la vue suivante
            request.session['csv_data'] = data
            return redirect('display_csv')  # Redirection vers la page d'affichage
    else:
        form = CSVUploadForm()

    return render(request, 'data_analyzer/upload.html', {'form': form})

# Vue pour afficher les données CSV et les statistiques
def display_csv(request):
    data = request.session.get('csv_data', None)
    filtered_data = None
    stats = None

    if data:
        headers = data[0]
        rows = data[1:]

        row_index = request.GET.get('row_index')
        col_name = request.GET.get('col_name')
        calculate_stats = request.GET.get('calculate_stats')

        if row_index is not None and row_index.isdigit():
            row_index = int(row_index)
            if 0 <= row_index < len(rows):
                filtered_data = [rows[row_index]]

        elif col_name:
            try:
                col_index = headers.index(col_name)
                filtered_data = [[row[col_index]] for row in rows]

                if calculate_stats:
                    col_values = [float(row[col_index]) for row in rows if row[col_index].replace('.', '', 1).isdigit()]
                    if col_values:
                        stats = {
                            'Moyenne': np.mean(col_values),
                            'Médiane': np.median(col_values),
                            'Variance': np.var(col_values),
                            'Écart type': np.std(col_values),
                            'Min': np.min(col_values),
                            'Max': np.max(col_values),
                        }

            except ValueError:
                filtered_data = None

    return render(request, 'data_analyzer/display.html', {
        'data': data,
        'filtered_data': filtered_data,
        'headers': data[0] if data else None,
        'stats': stats
    })

# Vue pour afficher les graphiques des données



def visualize_data(request):
    # Récupérer les données CSV depuis la session
    data = request.session.get('csv_data', None)
    df = None
    graph_html = None

    if data:
        try:
            headers = data[0]
            rows = data[1:]
            df = pd.DataFrame(rows, columns=headers)
            
            # Convertir les colonnes numériques
            for column in df.columns:
                try:
                    df[column] = pd.to_numeric(df[column], errors='coerce')
                except:
                    continue
            
            # Identifier les colonnes numériques
            numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
            
            plot_type = request.GET.get('plot_type', 'hist')
            column_name = request.GET.get('column')
            scatter_x = request.GET.get('scatter_x')
            scatter_y = request.GET.get('scatter_y')

            if plot_type == 'hist' and column_name and column_name in df.columns:
                fig = px.histogram(df, x=column_name)
                graph_html = fig.to_html(full_html=False)

            elif plot_type == 'line' and column_name and column_name in df.columns:
                fig = px.line(df, x=df.index, y=column_name)
                graph_html = fig.to_html(full_html=False)

            elif plot_type == 'scatter' and scatter_x and scatter_y:
                if scatter_x in df.columns and scatter_y in df.columns:
                    fig = px.scatter(df, x=scatter_x, y=scatter_y)
                    graph_html = fig.to_html(full_html=False)

            elif plot_type == 'boxplot' and column_name and column_name in df.columns:
                # Création du boxplot pour une colonne spécifique
                fig = px.box(df, y=column_name, points="all")
                fig.update_layout(
                    title=f'Boxplot de {column_name}',
                    yaxis_title=column_name,
                    showlegend=True
                )
                graph_html = fig.to_html(full_html=False)

            elif plot_type == 'heatmap' and numeric_columns:
                # Calculer la matrice de corrélation
                corr_matrix = df[numeric_columns].corr()
                
                # Créer le heatmap avec plotly
                fig = px.imshow(
                    corr_matrix,
                    labels=dict(color="Correlation"),
                    color_continuous_scale='RdBu_r',
                    aspect='auto'
                )
                
                # Mise à jour du layout
                fig.update_layout(
                    title='Matrice de corrélation',
                    xaxis_title="Variables",
                    yaxis_title="Variables",
                )
                
                graph_html = fig.to_html(full_html=False)

            elif plot_type == 'pairplot' and numeric_columns:
                try:
                    numeric_df = df[numeric_columns]
                    
                    if not numeric_df.empty:
                        plt.clf()
                        pair_plot = sns.pairplot(numeric_df)
                        
                        buf = BytesIO()
                        pair_plot.savefig(buf, format='png', bbox_inches='tight')
                        buf.seek(0)
                        
                        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                        graph_html = f'<img src="data:image/png;base64,{image_base64}" alt="Pairplot" style="width:100%;max-width:1000px">'
                        
                        plt.close('all')
                        buf.close()
                    else:
                        graph_html = "Pas de données numériques disponibles pour le pairplot."
                except Exception as e:
                    graph_html = f"Erreur lors de la création du pairplot: {str(e)}"

        except Exception as e:
            graph_html = f"Erreur lors du traitement des données: {str(e)}"

    else:
        graph_html = "Aucune donnée CSV chargée."

    return render(request, 'data_analyzer/visualize.html', {
        'graph_html': graph_html,
        'data': df if df is not None else pd.DataFrame()
    })