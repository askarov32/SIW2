from functions import topFivePopularNamesThisYear, getAllYears, getAllEthnicities, actionCount
from jinja2 import Template
import webbrowser


def main():
    dataset = "Popular_Baby_Names.csv"

    output_html = "output.html"

    with open(output_html, "w") as f:
        template_str = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Popular Baby Names</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container">
                <h1 class="mt-5 mb-4">Popular Baby Names</h1>
                <div class="mb-4">
                    <h2>Sorted list of all years in dataset:</h2>
                    <ul class="list-group">
                        {% for year in all_years %}
                            <li class="list-group-item">{{ year }}</li>
                        {% endfor %}
                    </ul>
                </div>
                <div class="mb-4">
                    <h2>Sorted list of all ethnicities in dataset:</h2>
                    <ul class="list-group">
                        {% for ethnicity in all_ethnicities %}
                            <li class="list-group-item">{{ ethnicity }}</li>
                        {% endfor %}
                    </ul>
                </div>
                <div class="mb-4">
                    <h2>Action Count: {{ action_count }}</h2>
                </div>
        
                {% if names %}
                    <div class="mb-4">
                        <h2>Top five popular names among {{ ethnicity }}s in {{ year }}</h2>
                        <ul class="list-group">
                            {% for name in names %}
                                <li class="list-group-item">{{ name }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                {% else %}
                    <div>
                        <p class="mb-4">No data available for the selected year or ethnicity.</p>
                    </div>
                {% endif %}
        
            </div>
        
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>

        """
        template = Template(template_str)

        names, year, ethnicity = topFivePopularNamesThisYear(dataset)

        f.write(template.render(all_years=getAllYears(dataset), all_ethnicities=getAllEthnicities(dataset),
                                action_count=actionCount(dataset),
                                names=names, year=year, ethnicity=ethnicity))

    print(f"Output written to {output_html}")
    webbrowser.open(output_html)

if __name__ == "__main__":
    main()
