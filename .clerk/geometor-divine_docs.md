


# GEOMETOR • divine


`geometor.divine` is a specialized library within the [GEOMETOR](https://geometor.com) initiative, dedicated to exploring and analyzing the golden ratio in geometric constructions.


Central to this module is the exploration of the golden ratio’s presence and significance in natural and mathematical structures. It leverages sophisticated algorithms and mathematical tools to uncover, analyze, and visualize the intricate ways in which the golden ratio manifests in various geometric forms.


Key functionalities of `geometor.divine` include:


* Identifying and analyzing golden sections in geometric models.
* Investigating chains of connected golden sections to reveal harmonic ranges.
* Grouping and categorizing golden sections based on size, segments, and points.
* Providing tools for in-depth exploration of the golden ratio in user-defined geometric constructions.


This module is designed to be intuitive yet powerful, catering to both enthusiasts and professionals in geometry, nature, and mathematics. Through its advanced analysis capabilities, `geometor.divine` aims to deepen the understanding of the golden ratio, offering a new perspective on its role and significance in the realm of geometry.


![_static/geometor-divine-overview.png](_static/geometor-divine-overview.png)

## recent logs


* 23.012 - [Defining the Divine Proportion](index.html#document-log/23.012-101550/index)


It is known by many names.
* 22.356 - [Welcome](index.html#document-log/22.356-152519)


first log entry for the system




### mission


Illuminate the mysteries of the golden ratio in geometry, offering advanced tools for in-depth analysis and exploration of its pervasive presence in nature and mathematics.


* Pioneer in geometric analysis with a focus on the golden ratio, uncovering its profound connections within nature and mathematics.
* Create intuitive, high-precision tools, enabling enthusiasts and experts alike to delve into and analyze the golden ratio’s role in geometric designs.
* Commit to the continual evolution of our understanding and applications of the golden ratio, keeping our methodologies and tools at the cutting edge of mathematical exploration.



#### goals


* 23.012 - [Defining the Divine Proportion](index.html#document-log/23.012-101550/index)


It is known by many names.
* 22.356 - [Welcome](index.html#document-log/22.356-152519)


first log entry for the system





### overview


`geometor.divine` is a specialized library within the [GEOMETOR](https://geometor.com) initiative, dedicated to exploring and analyzing the golden ratio in geometric constructions.


Central to this module is the exploration of the golden ratio’s presence and significance in natural and mathematical structures. It leverages sophisticated algorithms and mathematical tools to uncover, analyze, and visualize the intricate ways in which the golden ratio manifests in various geometric forms.


Key functionalities of `geometor.divine` include:


* Identifying and analyzing golden sections in geometric models.
* Investigating chains of connected golden sections to reveal harmonic ranges.
* Grouping and categorizing golden sections based on size, segments, and points.
* Providing tools for in-depth exploration of the golden ratio in user-defined geometric constructions.


This module is designed to be intuitive yet powerful, catering to both enthusiasts and professionals in geometry, nature, and mathematics. Through its advanced analysis capabilities, `geometor.divine` aims to deepen the understanding of the golden ratio, offering a new perspective on its role and significance in the realm of geometry.


![_static/geometor-divine-overview.png](_static/geometor-divine-overview.png)


### usage




### modules


* [geometor.divine](index.html#document-modules/geometor.divine)


Dedicated to the exploration and analysis of the golden ratio in geometry, geometor.divine offers a suite of tools for discovering and understanding this fundamental proportion in various geometric constructions.


The module comprises several submodules, each focusing on a unique aspect of golden ratio analysis, together forming a complete toolkit for in-depth exploration of its presence in geometric structures.
* [geometor.divine.golden](index.html#document-modules/geometor.divine.golden)


This submodule lies at the heart of the project, focusing on finding and analyzing golden sections in geometric models. It provides functions to identify golden sections in lines, points, and interconnected structures, facilitating comprehensive analysis of the golden ratio.
* geometor.divine.golden.chains


Specializing in the analysis of chains of connected golden sections, this submodule uncovers harmonic ranges and patterns within geometric models, offering insights into the sequential and relational aspects of golden sections.
* geometor.divine.golden.groups


Focused on grouping and categorizing golden sections, this submodule allows for sorting and analyzing golden sections based on various criteria such as size, segments, and points, enhancing the understanding of their distribution and relationships within geometric constructions.
* geometor.divine.golden.ranges


This submodule is dedicated to analyzing harmonic ranges and proportions within geometric models, particularly examining the relationships and ratios that define the golden ratio in various geometric contexts.




#### geometor.divine



##### divine





#### geometor.divine.golden


find and analyze golden sections



Todo


create a sections module





geometor.divine.golden.find\_golden\_sections\_in\_model(*model: Model*) → [tuple](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")[[list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section], [dict](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")[[sympy.geometry.line.Line](https://docs.sympy.org/latest/modules/geometry/lines.html#sympy.geometry.line.Line "(in SymPy v1.13.0rc2)"), [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]]]
analyze all lines in the model for golden sections





geometor.divine.golden.find\_golden\_sections\_in\_points(*pts*) → [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]
find golden sections in combinations of 3 points in list
returns a list of golden section pairs





geometor.divine.golden.is\_section\_golden(*section\_points*) → [bool](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")

Golden Chain Analyzer: Harmonic Range Identification in Golden Sections


This module is designed to analyze and explore chains of connected golden 
sections, unraveling the harmonic ranges within geometric structures. 
Utilizing sophisticated mathematical analysis and geometric algorithms, 
it aims to identify, categorize, and unpack chains, providing an intuitive 
understanding of their intrinsic geometric harmonies.


Features:


* find\_chains\_in\_sections: A function designed to meticulously identify 
chains within a collection of sections, resulting in a hierarchical tree 
structure representing connected sections.
* unpack\_chains: Unveils the chains hidden within the tree structure, 
outputting a list of individual Chain objects ready for analysis.


Each chain’s flow is characterized by the comparative lengths of consecutive
segments, represented symbolically to understand the progression and 
transitions in segment lengths. Furthermore, this module empowers users to 
explore symmetry lines within chains, unveiling a subtle, profound aspect of 
geometric harmony.




geometor.divine.golden.chains.find\_chains\_in\_sections(*sections: [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]*) → [dict](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")
Identify chains of connected golden sections to form harmonic ranges.



parameters:
`sections``list[Section]`A list of Section objects representing golden sections to be analyzed.





returns:
[`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")A dictionary representing a tree structure where each node is a
Section and connected Sections are child nodes.









geometor.divine.golden.chains.unpack\_chains(*tree: [dict](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")*) → [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.chains.Chain]
Unpack the chain tree into a list of individual Chain objects.



parameters:
`tree`[`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")A dictionary representing a tree structure where each node is a
Section and connected Sections are child nodes.





returns:
`list[Chain]`A list containing Chain objects, each representing a chain
of connected golden sections.









geometor.divine.golden.groups.group\_sections\_by\_size(*sections: [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]*) → [dict](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")[[sympy.core.expr.Expr](https://docs.sympy.org/latest/modules/core.html#sympy.core.expr.Expr "(in SymPy v1.13.0rc2)"), [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]]



geometor.divine.golden.groups.group\_sections\_by\_segments(*sections: [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]*) → [dict](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")[[sympy.geometry.line.Segment](https://docs.sympy.org/latest/modules/geometry/lines.html#sympy.geometry.line.Segment "(in SymPy v1.13.0rc2)"), [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]]



geometor.divine.golden.groups.group\_sections\_by\_points(*sections: [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]*) → [dict](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")[[sympy.geometry.point.Point](https://docs.sympy.org/latest/modules/geometry/points.html#sympy.geometry.point.Point "(in SymPy v1.13.0rc2)"), [list](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")[geometor.model.sections.Section]]



geometor.divine.golden.ranges.check\_range(*r*)



geometor.divine.golden.ranges.analyze\_harmonics(*line*)



geometor.divine.golden.ranges.analyze\_harmonics\_by\_segment(*sections\_by\_line*)





### demos




#### vesica



```
"""
constructs the classic 'vesica pisces'
"""
from geometor.model import \*
from geometor.model.helpers import \*
from geometor.render import \*

from geometor.divine import \*


def run():
    model = Model("vesica4a")
    A = model.set\_point(0, 0, classes=["given"])
    B = model.set\_point(1, 0, classes=["given"])

    model.construct\_line(A, B)

    model.construct\_circle(A, B)
    model.construct\_circle(B, A)

    C = model.get\_element\_by\_label("C")
    D = model.get\_element\_by\_label("D")
    E = model.get\_element\_by\_label("E")
    F = model.get\_element\_by\_label("F")

    model.set\_polygon([A, B, E])
    model.set\_polygon([A, B, F])

    model.construct\_line(E, F, classes=["red"])
    model.construct\_circle(A, D)
    model.construct\_circle(B, C)

    model.set\_wedge(A, B, F, E)

    # report\_summary(model)
    # report\_group\_by\_type(model)

    sequencer = Sequencer(model.name)
    # sequencer.plot\_sequence(model, extensions=['png'])
    sequencer.step\_sequence(model)
    plt.show()

    print("\nfind golden sections in model: \n")
    sections, sections\_by\_line = find\_golden\_sections\_in\_model(model)
    print(f"sections: {len(sections)}")
    for section in sections:
        # print(section.lengths)
        # print(section.ratio)
        # print(section.min\_length)
        # # print(section.points)
        print(section.get\_labels(model))

    chain\_tree = find\_chains\_in\_sections(sections)
    print(f"chains: {len(chain\_tree)}")
    chains = unpack\_chains(chain\_tree)
    for chain in chains:
        labels = ["\_".join(section.get\_labels(model)) for section in chain.sections]
        print()
        print(labels)
        print(len(chain.sections))

        print("points: ", chain.points)
        print("lengths: ", chain.lengths)
        print("floats: ", chain.numerical\_lengths)
        print("fibs: ", chain.fibonacci\_labels)

    print('flow: ')
    for chain in chains:
        labels = ["\_".join(section.get\_labels(model)) for section in chain.sections]
        print(chain.count\_symmetry\_lines(), chain.flow)

    # groups\_by\_size = group\_sections\_by\_size(sections)
    # print(groups\_by\_size)

    # plotter = Plotter(model.name)
    # plotter.plot\_model(model)
    # plot\_sections(plotter, model, sections)
    
    # plotter = Plotter(model.name)
    # plotter.plot\_model(model)
    # plot\_chains(plotter, model, chains)

    # groups = group\_sections\_by\_points(sections)
    # plotter = Plotter(model.name)
    # plotter.plot\_model(model)
    # title = "group sections by point"
    # plot\_groups(plotter, model, groups, title)

    # plt.show()

    report\_sequence(model)
    report\_sequence\_rst(model)



def report\_sequence\_rst(model, filename="model\_report.rst"):
 """Generate a sequential RST report of the model."""
    with open(filename, 'w') as file:
        file.write(f"MODEL Report: {model.name}\n")
        file.write("=" \* len(f"MODEL Report: {model.name}") + "\n\n")

        file.write(".. list-table:: Sequence\n")
        file.write(" :header-rows: 1\n\n")
        file.write(" \* - Label\n - <\n - >\n - Classes\n - Parents\n - Equation\n")

        for el, details in model.items():
            el\_classes = ', '.join(details.classes.keys())
            el\_parents = ', '.join(
                [f":math:`{model[parent].label}`" for parent in details.parents.keys()]
            )

            label = f":math:`{details.label}`"
            row = [
                label,
                "",
                "",
                el\_classes,
                el\_parents,
                "",
            ]
            if isinstance(el, spg.Point):
                row[1] = f":math:`{sp.latex(el.x)}`"
                row[2] = f":math:`{sp.latex(el.y)}`"

            elif isinstance(el, spg.Line):
                pt\_1, pt\_2 = el.points
                row[1] = f":math:`{model[pt\_1].label or pt\_1}`"
                row[2] = f":math:`{model[pt\_2].label or pt\_2}`"
                row[5] = f":math:`{sp.latex(el.equation())}`"

            elif isinstance(el, spg.Circle):
                pt\_center = el.center
                pt\_radius = details.pt\_radius
                row[1] = f":math:`{model[pt\_center].label or pt\_center}`"
                row[2] = f":math:`{model[pt\_radius].label or pt\_radius}`"
                row[5] = f":math:`{sp.latex(el.equation())}`"

            elif isinstance(el, spg.Segment) or isinstance(el, spg.Polygon):
                vertices = ', '.join([f":math:`{model[pt].label or pt}`" for pt in el.vertices])
                row[1] = vertices

            file.write(" \* - " + "\n - ".join(row) + "\n")




if \_\_name\_\_ == "\_\_main\_\_":
    run()

```






### logs


* 23.012 - [Defining the Divine Proportion](index.html#document-log/23.012-101550/index)


It is known by many names.


[*more*](index.html#document-log/23.012-101550/index)
* 22.356 - [Welcome](index.html#document-log/22.356-152519)


first log entry for the system


[*more*](index.html#document-log/22.356-152519)




### references






### todos



Todo


create a sections module



(The [*original entry*](index.html#id1) is located in /home/phiarchitect/PROJECTS/geometor/divine/src/geometor/divine/golden/\_\_init\_\_.py:docstring of geometor.divine.golden, line 3.)




### changelog



#### 0.1.0


*2023-11-15*


**fixed**


**added**


**changed**





### glossary



testa test item






### contribute




### discuss




### About GEOMETOR






## indices


* [Index](genindex.html)
* [Module Index](py-modindex.html)
* [Search Page](search.html)







