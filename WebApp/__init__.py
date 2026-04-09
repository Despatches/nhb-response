import os

from flask import Flask, render_template,Response

from jinja2 import Template

from .config import Config
from .shorthand import shorts as shorthand_names

#from weasyprint import HTML, default_url_fetcher
#import mimetypes


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


    def render_with_terms(url_path, components = []):
        return render_template(
            url_path, 
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
            VARS = "<b>Vendor, Agent, Reseller, Surveyor</b>",
            NatHB = "<b>National Homebuyers</b>",
            AAI = "Agent Auction or Intermediary",
            FF = "Furnace Farm",
            OH = "Oliver Hume",
            EH = "Edward Hume",
            MI = "Material Information",
            BMPA = "Barnard Marcus Property Auctioneers",
            UPB = "un-verified viewing Prospective buyer",
            OPB = "<b> verified Onboarded prospective buyer</b>",
            DMB = "Disclosures, Marketing & Brochures",
            CPR = "Civil Procedure Rules (CPR)",
            FB = { 
                "U" : "Facebook User",
                "P" : "Facebook Page Content Publisher",
                "M" : "Facebook Moderator",
                "O" : "Facebook Site Owner",
                "C" : "Facebook Corporation",
            },
            FBAG = "'Anything Goudhurst. Information, Buy & Sell, Jobs' facebook page",
            LegalTerm = {
                "DOC" : "Duty of Care",
                "MC2DPM" : "... to Disclose ..",
                "PMA" : "... to Disclose ..",
                "CPRR" : "CPR Regulation ref.:",
            }
        );        
    
    print("basic function")

    @app.route('/intro')
    def intro():

        lit_motive_path = "sections/litigation_motive"

        components = [
            {
                "id": "intro",
                "label": "Introduction",
                "dynamic" : "sections/main_intro.jinja",
                "subsections": [
                    {
                        "id": "intro_sub1", "label": "Background","dynamic" : "sections/background.jinja",
                    },
                    {
                        "id": "intro_sub2", 
                        "label": "Purpose"
                    },
                    {
                        "label" :"Farmhouse Title Facts",
                        "id" : "fhouse_title_facts",
                        "dynamic" : "sections/fhouse_title_facts.jinja",
                        #"lit_exhibit" : True,
                    },
                ]
            },
            {
                "label" :"NHB Litigation Motive",
                "id" : "litigation_motive",
                "dynamic" : f"{lit_motive_path}/litigation_motive.jinja",
                "subsections": [
                    {
                        "id" : "accusation",
                        "label" : "Accusation",
                        "dynamic" : f"{lit_motive_path}/accusation.jinja",
                    },
                    {
                        "id" : "fiction",
                        "label" : "Fiction",
                        "dynamic" : f"{lit_motive_path}/fiction.jinja",
                    },
                    {
                        "id" : "fact",
                        "label" : "Fact",
                        "dynamic" : f"{lit_motive_path}/fact.jinja",
                    },
                    {
                        "id" : "realities",
                        "label" : "Realities",
                        "dynamic" : f"{lit_motive_path}/realities.jinja",
                    }
                ]
                #"lit_exhibit" : True,
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
                "label" :"Dishonesty",
                "id" : "dishonesty",
                "dynamic" : "sections/dishonesty.jinja",
                #"lit_exhibit" : True,
            },           
            {
                "label" :"Crime",
                "id" : "crime",
                "dynamic" : "sections/crime.jinja",
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
                "dynamic" : "sections/pollution_risks.jinja",
                "subsections": []
            },
            {
                "id": "flood_risks",
                "label": "Flood Risk",
                "dynamic" : "sections/flood_risks.jinja",
                "subsections": []
            },

            {
                "id": "defamation_act_sec.5_web_operators",
                "label": "Defamation Web Operators",
                "dynamic" : "defamation_act/defamation_act_sec.5_web_operators.jinja",
                "subsections": []
            },
            {
                "id": "imminent_harm",
                "label": "Imminent Harm",
                "dynamic" : "sections/imminent_harm.jinja",
                "subsections": []
            },
            {
                "id": "imminent_harm",
                "label": "Imminent Harm",
                "dynamic" : "sections/imminent_harm.jinja",
                "subsections": []
            },
            {
                "id": "listed_compliance",
                "label": "Listed Building Compliance",
                "dynamic" : "defence/twbc/planning_enf_issues/twbc_listed_building_planning_enforcement.jinja",
                "subsections": []
            },
            {
                "id": "review_manipulation",
                "label": "Review Manipulation",
                "dynamic" : "sections/review_buying/basic.jinja",
                "subsections": []
            },
            {
                "id": "conclusion",
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
            "my_table" : {
                "headings" : ["heading1","heading2","heading3"],
                "content" : [
                    ["tyms","650000","october"],
                    ["tyms","650000","october"],
                    ["tyms","650000","october"],
                ]
            }
        }

        table2 = {
            "my_table" : {
                "headings" : ["heading1","heading2","heading3"],
                "content" : [
                    {
                        "date" : "<the row text>",
                        "name" : "<row_context>",
                        "price" : "<the row text>"
                    },
                    {

                    }
                ]
            }
        }

        return render_with_terms('intro.html',components)

    def make_url_fetcher(app):
        def url_fetcher(url):

            # catch both /static/ and http://127.0.0.1.../static/
            if '/static/' in url:
                static_part = url.split('/static/', 1)[1]
                file_path = os.path.join(app.static_folder, static_part)
                mime_type, _ = mimetypes.guess_type(file_path)
                with open(file_path, 'rb') as f:
                    return {
                        'string': f.read(),
                        'mime_type': mime_type or 'application/octet-stream',
                    }

            return default_url_fetcher(url)
        return url_fetcher

    @app.route('/print/intro')
    def print_intro():
        html_string = intro()

        pdf = HTML(
            string=html_string,
            base_url='http://127.0.0.1:5000',
            url_fetcher=make_url_fetcher(app)
        ).write_pdf()

        return Response(
            pdf,
            mimetype='application/pdf',
            headers={'Content-Disposition': 'inline; filename=intro.pdf'}
        )

    @app.route("/counterclaim")
    def counter_claim():
        components = [
            {
                "id": "exibits",
                "label": "Exibits",
                "subsections": [],
                "dynamic" : "counter_claim/exibits.jinja",
            }
        ];
        return render_template('intro.html',components=components)

    @app.route('/')
    def hello():
        return render_template('intro.html')





    def render_letter(url_path):
        letter_content = render_with_terms(url_path)
        return render_template(
            "letters/base_letter.jinja",
            content = letter_content,
            communicator_name = "We are the liberation front",
            telephone = "077857864",
            email="libfront@bastards.com"
        )

    @app.route('/letter/<wanted_letter>')
    def RenderLetter(wanted_letter):

        letters = {
            "nhb_disclosure" :  'defence/adr_request_list/required_from_nhb.jinja',
            "facebook_request" : 'facebook/letter_facebook.jinja',
            "dsar_letter" : "facebook/dsar_letter.jinja",
            "listed_compliance" : 'defence/twbc/planning_enf_issues/twbc_listed_building_planning_enforcement.jinja',
            "hjoad":"letters/hjoad.08_04_2026_harassment_i"
        }

        url_path = ""
        if wanted_letter in letters:
            url_path = letters[wanted_letter]

        if url_path != "":
            return render_letter(url_path)



    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return "404";

    return app
