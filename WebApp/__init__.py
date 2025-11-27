import os

from flask import Flask, render_template

from .config import Config
from .shorthand import shorts as shorthand_names


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    '''app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )'''

    app.config.from_object(Config)


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello

    print("basic function")
    @app.route('/intro')
    def intro():
        components = [
            {
                "id": "intro",
                "label": "Introduction",
                "dynamic" : "sections/main_intro.jinja",
                "subsections": [
                    {
                        "id": "intro_sub1", "label": "Background","dynamic" : "sections/background.jinja",
                    },
                    {"id": "intro_sub2", "label": "Purpose"},
                     {
                        "label" :"Farmhouse Title Facts",
                        "id" : "fhouse_title_facts",
                        "dynamic" : "sections/fhouse_title_facts.jinja",
                        #"lit_exhibit" : True,
                    },
                    {
                        "label" :"NHB Litigation Motive",
                        "id" : "litigation_motive",
                        "dynamic" : "sections/litigation_motive.jinja",
                        #"lit_exhibit" : True,
                    },
                ]
            },
             {
                "label" :"NHB Disclosure",
                "id" : "disclosure_nhb",
                "dynamic" : "sections/disclosure_nhb.jinja",
                #"lit_exhibit" : True,
            },
            {
                "label" :"Boundaries",
                "id" : "boundary",
                "dynamic" : "sections/boundaries.jinja",
                #"lit_exhibit" : True,
            },
            {
                "label" :"Abandoned and Waste Materials",
                "id" : "abandonment_and_waste",
                "dynamic" : "sections/abandonment_and_waste.jinja",
                "subsections": [
                    {
                        "label" :"analysis of Exhibit NHBE-a",
                        "id" : "exhibit-NHBE-a",
                        "dynamic" : "sections/exhibit_analysis/exhibit-NHBE-a.jinja",
                        #"lit_exhibit" : True,
                    },   
                    {
                        "label" :"analysis of Exhibit NHBE-b",
                        "id" : "exhibit-NHBE-b",
                        "dynamic" : "sections/exhibit_analysis/exhibit-NHBE-b.jinja",
                        #"lit_exhibit" : True,
                    }, 
                    {
                        "label" :"analysis of Exhibit NHBE-c",
                        "id" : "exhibit-NHBE-c",
                        "dynamic" : "sections/exhibit_analysis/exhibit-NHBE-c.jinja",
                        #"lit_exhibit" : True,
                    },  
                    {
                        "label" :"analysis of Exhibit NHBE-d",
                        "id" : "exhibit-NHBE-d",
                        "dynamic" : "sections/exhibit_analysis/exhibit-NHBE-d.jinja",
                        #"lit_exhibit" : True,
                    },               
                ]
            },
            {
                "label" :"General trespass and nuisance",
                "id" : "general_trespass",
                "dynamic" : "sections/general_trespass.jinja",
                 "subsections": [
                    {
                        "label" :"Gate",
                        "id" : "gate",
                        "dynamic" : "sections/gate.jinja",
                        #"lit_exhibit" : True,
                    },
                 ]
                #"lit_exhibit" : True,
            },            
            {
                "label" :"Dumped Garden Waste",
                "id" : "dumped",
                "dynamic" : "sections/dumped.jinja",
                #"lit_exhibit" : True,
            },
            {
                "label" :"Neglect",
                "id" : "neglect",
                "dynamic" : "sections/neglect.jinja",
                #"lit_exhibit" : True,
            },
            {
                "id": "facts",
                "label": "Statement of Facts",
                "subsections": []
            },
            {
                "id": "grounds",
                "label": "Grounds of Defence",
                "subsections": [
                    {
                        "id": "grounds_sub1",
                        "label": "Legal Grounds"
                    },
                    {"id": "grounds_sub2", "label": "Procedural Grounds"}
                ]
            },
            {
                "id": "evidence",
                "label": "Supporting Evidence",
                "subsections": []
            },
            {
                "id": "social_media_response",
                "label": "Social Media Campaign",
                "subsections": [],
                "dynamic" : "sections/social_media_response.jinja",
            },
            {
                "id" : "property_value",
                "label" :"property value",
                "dynamic" : "sections/property_value.jinja",
            },
            {
                "id": "pollution_risks",
                "label": "Pollution Risk",
                "subsections": []
            },
            {
                "id": "conclusion",
                "label": "Conclusion",
                "subsections": []
            },
            {
                "id": "exibits",
                "label": "Exibits",
                "subsections": [],
                "dynamic" : "sections/exibits.jinja",
                "subsections": [
                    {
                        "id" : "letter_exibits",
                        "label" :"Corespondence Exhibits",
                        "dynamic" : "sections/letter_exhibits.jinja",                    
                    }
                ]
            }
        ]

        tables = {
            "my_table" : [
                [],
                []
            ]
        }
        return render_template(
            'intro.html', 
            components=components, 
            deeds = 'images/deeds/',
            claim_letter = 'images/nhb_claim_letter/', 
            claim_images = 'images/nhb_claim_images/',
            marketing = 'images/FFH_marketing_photos/', 
            diagrams = 'images/general_diagrams/',
            MM = "<b>Mansell Mctaggart Estate Agents</b>",
            FFH = "<b>Furnace Farm House</b>",
            FFHO = "<b> Furnace Farmhouse Owner or Occupier</b>",
            MMAM = "<b>Momentum Asset Management</b>",
            NHB = "<b>NHB Investments Limited</b>",
            NatHB = "<b>National Homebuyers</b>",
            FF = "Furnace Farm",
            OH = "Oliver Hume",
            EH = "Edward Hume",
            MI = "Material Information",
            BMPA = "Barnard Marcus Property Auctioneers",
            UPB = "usnverified viewing Prospect",
            OPB = "<b>Onboarded verified viewing prospect</b>",
            FBAG = "'Anything Goudhurst. Information, Buy & Sell, Jobs' facebook page",
            LegalTerm = {
                "DOC" : "Duty of Care",
            }

        );
    @app.route('/')
    def hello():
        return render_template('intro.html')

    @app.route('/letter')
    def renderletter():
        return render_template('letters/odt_nhb.27_nov_2025.adr.html',
            deeds = 'images/deeds/',
            claim_letter = 'images/nhb_claim_letter/', 
            claim_images = 'images/nhb_claim_images/',
            marketing = 'images/FFH_marketing_photos/', 
            diagrams = 'images/general_diagrams/',
            MM = "<b>Mansell Mctaggart Estate Agents</b>",
            FFH = "<b>Furnace Farm House</b>",
            FFHO = "<b> Furnace Farmhouse Owner or Occupier</b>",
            MMAM = "<b>Momentum Asset Management</b>",
            NHB = "<b>NHB Investments Limited</b>",
            NatHB = "<b>National Homebuyers</b>",
            FF = "Furnace Farm",
            OH = "Oliver Hume",
            EH = "Edward Hume",
            MI = "Material Information",
            BMPA = "Barnard Marcus Property Auctioneers",
            UPB = "usnverified viewing Prospect",
            OPB = "<b>Onboarded verified viewing prospect</b>",
            FBAG = "'Anything Goudhurst. Information, Buy & Sell, Jobs' facebook page",
            LegalTerm = {
                "DOC" : "Duty of Care",
            })


    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return "404";

    return app
