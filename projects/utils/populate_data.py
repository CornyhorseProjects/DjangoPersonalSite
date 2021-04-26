from projects import models as m


def insert_by_title(title, description, body, image, detail_image=None):
    print("Attempting to update first...")
    updated_rows = m.Project.objects.filter(title=title).update(
        title=title,
        description=description,
        body=body,
        image=image,
        detail_image=detail_image,
    )

    if not updated_rows:
        print("Adding project: Business & Technology...")
        p = m.Project(
            title=title,
            description=description,
            body=body,
            image=image,
        )
        p.save()


def projects():
    body = """<p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer aliquam urna sed leo tempor 
    feugiat. Vestibulum ante sapien, vulputate non quam eget, iaculis pretium tellus. Mauris 
    egestas, velit ultricies porta accumsan, quam nunc dictum massa, sagittis placerat odio massa 
    nec sem. Quisque id molestie tellus. Donec sit amet diam faucibus, efficitur ante eget, 
    tincidunt ipsum. Donec quis purus in odio rutrum placerat. Vestibulum lacus est, posuere quis 
    erat eget, egestas scelerisque turpis. Praesent in libero id arcu aliquet finibus. Aenean 
    malesuada cursus porta. Aliquam mollis turpis eu ullamcorper porta. Cras venenatis, nulla et 
    lacinia congue, felis purus placerat nibh, nec dictum nibh metus vehicula lorem. Cras eget 
    tellus bibendum, elementum mi vel, cursus eros.</p>
    
    <h2>Maecenas Scelerisque:</h2>
    <ul>
    <li>Quisque Vestibulum
    <li>Phasellus Donec 
    <li>Sed Ultrices 
    <li>Pellentesque Lacinia 
    <li>Feugiat, Rutrum, & Interdum 
    <li>Convallis Varius (Maecenas elementum turpis)
    </ul>
    
    <h3>Aenean Vulputate:</h3>
    <table style="width:100%;">
    <tr><th style="text-align:left">Aliquam:</th><td>Ullamcorper</td><td>SQL</td><td>Porttitor
    </td></tr>
    <tr><th  style="text-align:left">Facilisis:</th><td>Feugiat</td><td>Gravida</td><td
    >Commodo</tr>
    <tr><th  style="text-align:left">Curabitur 
    pretium:</th><td>PostgreSQL</td><td>Oracle</td><td>SQL 
    Server</td><td>MySQL</td><td>SQLite</td></tr>
    
    
    </table>
    <br>
    <h2>Lacus Porttitor</h2>
        <ul>
    <li>Nonodio Vestibulum
        <ul>
        <li>Donec non Justo Malesuada
        <li>Proin ut sem vel
        </ul>
    <li>Phasellus eget ligula
        <ul>
        <li>Volutpat Pharetra non nec Libero
        <li>Nulla Blandit Nulla eu Rhoncus Mollis
        </ul>

    
    """

    insert_by_title(
        title="Maecenas Scelerisque",
        description="",
        body=body,
        image="img/visualization.jpg",
        detail_image="img/code3.jpg",
    )

    ### Insert Second Subject:

    body = """<p>Phasellus sem risus, rutrum sed semper sed, dapibus id justo. Donec eget tellus 
    a diam mollis auctor non eu odio. Aliquam ut venenatis orci, id tincidunt purus. Vivamus sem 
    urna, consectetur sit amet metus vel, luctus efficitur libero. Nullam scelerisque facilisis 
    tortor in faucibus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur 
    ridiculus mus. Cras lobortis tristique lacus sit amet tempus. Pellentesque egestas, magna id 
    rhoncus tincidunt, ligula lectus blandit dui, vel vulputate elit eros vel arcu. Etiam vitae 
    odio ut odio tempus tincidunt in sit amet libero. Morbi dignissim finibus tellus id rhoncus. 
    Curabitur sodales mauris a turpis tristique, eu hendrerit ex vulputate. Sed dapibus sem id 
    lacus congue pellentesque. Quisque sed accumsan turpis. Donec vel purus tempor, sodales dui 
    in, congue ipsum. Ut lobortis vel lacus eu vulputate.</p>

<p>Nam in nulla sed nisi elementum hendrerit ut a dolor. Morbi a efficitur arcu. Cras vulputate 
porttitor condimentum. Fusce venenatis porta tristique. Phasellus convallis nulla nec risus 
suscipit sollicitudin. Donec quis lorem odio. Nulla malesuada ex venenatis, dignissim urna eget, 
imperdiet metus. Maecenas nec sodales tortor. Nullam scelerisque mi nec nibh maximus lobortis. 
Aenean venenatis, nibh a aliquet malesuada, turpis enim dictum justo, sed vehicula justo ipsum 
vulputate nibh. Vestibulum fermentum odio ac felis tincidunt commodo. Donec sed sem quis risus 
cursus porta id eu risus. Aenean accumsan porttitor massa, non faucibus erat blandit sed. In 
feugiat nec odio tempus fermentum.</p>


    <h2>Etiam ut Leo At Tortor</h2>
    <ul>
    <li>Duis tempor mauris non augue venenatis mattis
    <li>Nam laoreet purus at ullamcorper viverra
    </ul>
    
    <h3>Nam luctus felis:</h3>
    <ul>
    <li>Cras id nisi placerat ipsum condimentum interdum
    <ul>
    
    """
    insert_by_title(
        title="Fusce Tristique",
        description="",
        body=body,
        image="img/black-coffee-business-cellphone-860379.jpg",
        detail_image="img/ben-kolde-430909-unsplash.jpg",
    )
