# api/views.py

import base64
from io import BytesIO

import plotly.graph_objects as go
import plotly.io as pio
from django.http import HttpRequest, HttpResponse
from ninja import Router
from weasyprint import HTML

router = Router()


@router.post("/generate-pdf/")
def generate_pdf(request: HttpRequest) -> HttpResponse:
    """Generate a PDF containing a Plotly graph.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object (not used in this function).

    Returns
    -------
    HttpResponse
        A response containing the generated PDF as its content.

    """
    print(request, type(request))
    # グラフ生成 Plotly
    fig = go.Figure(data=[go.Bar(y=[4, 1, 3])])
    img_bytes = pio.to_image(fig, format="png")
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    # HTML生成 WeasyPrintでPDF化
    html = f"""
    <html>
      <body>
        <h1>Thaleia レポート</h1>
        <p>これは自動生成されたPDFです。</p>
        <img src="data:image/png;base64,{img_base64}" />
      </body>
    </html>
    """

    pdf_io = BytesIO()
    HTML(string=html).write_pdf(pdf_io)
    return HttpResponse(pdf_io.getvalue(), content_type="application/pdf")
