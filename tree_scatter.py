"""
tree_scatter.py
creates a random tree of a random size and orientation from selected vertices
by Luna Sosa
created: 11.5.23
last modified: 11.15.23

** find this code and more at lunasosaart.myportfolio.com/coding-for-maya **

MEANT TO WORK WITH MAYA 2022

Script meant to work when one independently creates a maya plane and selects vertices on it.
Will also generate a skydome and directional lights that are best seen through the Arnold renderview
"""

import maya.cmds as cmds
import random

PFX = "LS_"

# MAIN #


def mk_tree1(itt):
    # create tree base #
    cmds.polyCylinder(n=f"{PFX}tree1_{itt:02}_base1", r=.5, sx=10, sy=4)  # base 1
    # set pivot to base
    cmds.xform(piv=(0, -1, 0))
    cmds.move(0, 1, 0, r=1)
    cmds.scale(1.3, 4.5, 1.3)
    cmds.DeleteHistory()
    cmds.FreezeTransformations()

    cmds.select(f"{PFX}tree1_{itt:02}_base1")
    cmds.scale(1.3, .3, 1.3)

    # create branches
    cmds.polyExtrudeFacet(f"{PFX}tree1_{itt:02}_base1.f[41]", ls=(.8, .8, .8), t=(1, 3, -.5))
    cmds.polyExtrudeFacet(f"{PFX}tree1_{itt:02}_base1.f[41]", ls=(.8, .8, .8), t=(-.5, 8, .5))

    cmds.polyCylinder(n=f"{PFX}tree1_{itt:02}_base1", r=.4, sx=10, sy=4)
    cmds.move(0, 9, -.57)
    cmds.scale(1, 1.8, 1)
    cmds.rotate(-4, 1.6, 29)
    cmds.polyExtrudeFacet(f"{PFX}tree1_{itt:02}_base1.f[41]", ls=(.9, .9, .9), t=(-.5, 2, 0), d=4)
    cmds.polyExtrudeFacet(f"{PFX}tree1_{itt:02}_base1.f[41]", ls=(.9, .9, .9), t=(-1, 2, 0), d=4)

    cmds.polyCylinder(n=f"{PFX}tree1_{itt:02}_base2", r=.5, sx=10, sy=4)  # base 2
    cmds.move(1.5, 15.4, 0.443, r=1)
    cmds.scale(.7, 1.6, .7)
    cmds.rotate(20, 0, -42)

    cmds.select(f"{PFX}tree1_{itt:02}_base2")  # base 3
    cmds.duplicate()
    cmds.select(f"{PFX}tree1_{itt:02}_base2")  # base 4
    cmds.move(1.09, 3.16, -.5, r=1)
    cmds.rotate(-30, 0, -16)
    cmds.scale(1, 1.46, 1)

    # create shader, apply, and group tree bits
    tree_grp = cmds.group(empty=1, n=f"{PFX}tree1_{itt:02}_base")
    tree_obj_color = cmds.shadingNode('standardSurface', n=f"{PFX}base_shd", asShader=1)
    cmds.setAttr(tree_obj_color + ".baseColor", 0.1, .07, .06)

    for k in range(4):
        tree = f"{PFX}tree1_{itt:02}_base" + str(k + 1)
        cmds.parent(tree, tree_grp)
        cmds.select(f"{PFX}tree1_{itt:02}_base" + str(k + 1))
        cmds.hyperShade(assign=tree_obj_color)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

    # create leaves #
    cmds.polySphere(n=f"{PFX}tree1_{itt:02}_leaf1", r=2, sx=8, sy=8)  # leaf 1
    cmds.move(2.26, 17.7, 0, r=1)
    cmds.select(f"{PFX}tree1_{itt:02}_leaf1.f[21]", f"{PFX}tree1_{itt:02}_leaf1.f[29]",
                f"{PFX}tree1_{itt:02}_leaf1.f[36]")
    cmds.move(-.7, 0, .55, r=1)
    cmds.scale(0.77, 1, 0.77)
    cmds.select(f"{PFX}tree1_{itt:02}_leaf1.f[37:38]", f"{PFX}tree1_{itt:02}_leaf1.f[46:47]")
    cmds.move(.2, .4, -.2, r=1)
    cmds.select(f"{PFX}tree1_{itt:02}_leaf1.f[22]", f"{PFX}tree1_{itt:02}_leaf1.f[30]")
    cmds.move(0, -.55, 0, r=1)

    # duplicate the leaf to make a block
    cmds.select(f"{PFX}tree1_{itt:02}_leaf1")
    cmds.duplicate()  # leaf 2
    cmds.scale(.8, .9, .9)
    cmds.move(-2.7, 2, .6, r=1)
    cmds.rotate(-45, 0, 0)
    cmds.duplicate()  # leaf 3
    cmds.rotate(60, -45, 0)
    cmds.move(1.15, 1, -2, r=1)
    cmds.DeleteHistory()
    cmds.FreezeTransformations()

    # create other blocks
    cmds.select(f"{PFX}tree1_{itt:02}_leaf1", f"{PFX}tree1_{itt:02}_leaf2", f"{PFX}tree1_{itt:02}_leaf3")
    cmds.duplicate()  # leaf 4, 5, 6
    cmds.move(-3, -7, -2, r=1)
    # cmds.rotate(-45,60,-70)
    cmds.select(f"{PFX}tree1_{itt:02}_leaf5")
    cmds.move(5, 1, 0, r=1)
    cmds.select(f"{PFX}tree1_{itt:02}_leaf6")
    cmds.move(2.2, .2, 1.7, r=1)

    cmds.select(f"{PFX}tree1_{itt:02}_leaf4", f"{PFX}tree1_{itt:02}_leaf5", f"{PFX}tree1_{itt:02}_leaf6")
    cmds.duplicate()  # leaf 7, 8, 9
    cmds.move(-1.5, 3.5, -.8, r=1)

    # refine leaf positions
    cmds.select(f"{PFX}tree1_{itt:02}_leaf6")
    cmds.move(3.64, 1, 0, r=1)
    cmds.select(f"{PFX}tree1_{itt:02}_leaf7")
    cmds.move(.8, 0, .7, r=1)
    cmds.select(f"{PFX}tree1_{itt:02}_leaf2")
    cmds.move(0, -.85, 0, r=1)
    cmds.DeleteHistory()
    cmds.FreezeTransformations()

    # create shader, apply, and group leaf bits
    leaf_grp = cmds.group(empty=1, n=f"{PFX}tree1_{itt:02}_leaves")
    leaf_obj_color = cmds.shadingNode('standardSurface', n=f"{PFX}tree3_{itt:02}_leaf_shd", asShader=1)
    
    # REPLACE WITH RANGE OF VALUES ONCE YOU GET HOME #
    # randomize leaf hue
    r_color = random.uniform(0.13)
    g_color = random.uniform(.05)
    b_color = random.uniform(.15)
    cmds.setAttr(leaf_obj_color + ".baseColor",r_color, g_color, b_color)

    for j in range(9):
        leaf = f"{PFX}tree1_{itt:02}_leaf" + str(j + 1)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.parent(leaf, leaf_grp)
        cmds.select(f"{PFX}tree1_{itt:02}_leaf" + str(j + 1))
        cmds.hyperShade(assign=leaf_obj_color)

    # cleanup
    cmds.select(f"{PFX}tree1_{itt:02}_base", f"{PFX}tree1_{itt:02}_leaves")
    cmds.DeleteHistory()
    cmds.FreezeTransformations()

    curr_grp = cmds.group(n=f"{PFX}tree1_{itt:02}_GRP", empty=1)
    cmds.parent(f"{PFX}tree1_{itt:02}_leaves", f"{PFX}tree1_{itt:02}_base")
    cmds.parent(f"{PFX}tree1_{itt:02}_base", f"{PFX}tree1_{itt:02}_GRP")

    return cmds.move(0, 0, 0, curr_grp + ".scalePivot")


def mk_tree2(itt):
    # create tree base #
    cmds.polyCylinder(n=f"{PFX}tree2_{itt:02}_base1", r=.7, sx=10, sy=4)  # base 1
    # set pivot to base
    cmds.xform(piv=(0, -1, 0))
    cmds.move(0, 1, 0, r=1)
    cmds.scale(1.3, 2, 1.3)

    cmds.select(f"{PFX}tree2_{itt:02}_base1.f[0:9]")
    cmds.scale(1.5, .3, 1.5)

    cmds.polyExtrudeFacet(f"{PFX}tree2_{itt:02}_base1.f[41]", ls=(.9, .9, .9), t=(0, 5, 0))
    cmds.polyExtrudeFacet(f"{PFX}tree2_{itt:02}_base1.f[41]", ls=(.9, .9, .9), t=(1.6, 5, 0))

    # create branch
    cmds.polyCylinder(n=f"{PFX}tree2_{itt:02}_base2", r=.6, sx=10, sy=4)  # base 2
    cmds.move(-1.4, 11.54, 0, r=1)
    cmds.rotate(0, 0, 30)
    cmds.scale(1, 3, 1)

    # create shader, apply, and group tree bits
    tree_grp = cmds.group(empty=1, n=f"{PFX}tree2_{itt:02}_base")
    tree_obj_color = cmds.shadingNode('standardSurface', n=f"{PFX}base_shd", asShader=1)
    cmds.setAttr(tree_obj_color + ".baseColor", 0.13, .07, .11)

    for i in range(2):
        tree = f"{PFX}tree2_{itt:02}_base" + str(i + 1)
        cmds.parent(tree, tree_grp)
        cmds.select(f"{PFX}tree2_{itt:02}_base" + str(i + 1))
        cmds.hyperShade(assign=tree_obj_color)

    # create leaves #
    cmds.polySphere(n=f"{PFX}tree2_{itt:02}_leaf1", r=2, sx=8, sy=8)  # leaf 1
    cmds.move(2.26, 14, 0, r=1)
    cmds.select(f"{PFX}tree2_{itt:02}_leaf1.f[21]", f"{PFX}tree2_{itt:02}_leaf1.f[29]",
                f'{PFX}tree2_{itt:02}_leaf1.f[36]')
    cmds.move(-.7, 0, .55, r=1)
    cmds.scale(0.77, 1, 0.77)
    cmds.select(f"{PFX}tree2_{itt:02}_leaf1.f[37:38]", f'{PFX}tree2_{itt:02}_leaf1.f[46:47]')
    cmds.move(.2, .4, -.2, r=1)
    cmds.select(f"{PFX}tree2_{itt:02}_leaf1.f[22]", f'{PFX}tree2_{itt:02}_leaf1.f[30]')
    cmds.move(0, -.55, 0, r=1)

    # duplicate the leaf to make a block
    cmds.select(f"{PFX}tree2_{itt:02}_leaf1")
    cmds.duplicate()  # leaf 2
    cmds.move(0, -1.7, -1.76, r=1)
    cmds.rotate(0, 0, -67)
    cmds.select(f"{PFX}tree2_{itt:02}_leaf2")
    cmds.duplicate()  # leaf 3
    cmds.move(-2.3, 1.5, 0, r=1)
    cmds.rotate(0, 0, -180)

    # create other blocks
    cmds.select(f"{PFX}tree2_{itt:02}_leaf1", f"{PFX}tree2_{itt:02}_leaf2", f"{PFX}tree2_{itt:02}_leaf3")
    cmds.duplicate()  # leaf 4, 5, 6
    cmds.move(-5.6, 3.13, 0.9, r=1)
    cmds.select(f"{PFX}tree2_{itt:02}_leaf5")
    cmds.rotate(28, 38, -168, r=1)

    cmds.select(f"{PFX}tree2_{itt:02}_leaf4", f"{PFX}tree2_{itt:02}_leaf5", f"{PFX}tree2_{itt:02}_leaf6")
    cmds.duplicate()  # leaf 7, 8, 9
    cmds.move(4.2, 0, 0.9, r=1)
    cmds.rotate(-48, 0, 0, r=1)

    cmds.select(f"{PFX}tree2_{itt:02}_leaf7", f"{PFX}tree2_{itt:02}_leaf8", f"{PFX}tree2_{itt:02}_leaf9")
    cmds.duplicate()  # leaf 10, 11, 12
    cmds.move(0, 2.8, -1.6, r=1)
    cmds.rotate(45, 0, 12, r=1)

    cmds.select(f"{PFX}tree2_{itt:02}_leaf10", f"{PFX}tree2_{itt:02}_leaf11", f"{PFX}tree2_{itt:02}_leaf12")
    cmds.duplicate()  # leaf 13, 14, 15
    cmds.move(4.4, -3.4, -0.9, r=1)

    # refine leaf positions
    cmds.select(f"{PFX}tree2_{itt:02}_leaf13")
    cmds.move(-5.6, 0.15, -3.2, r=1)
    cmds.select(f"{PFX}tree2_{itt:02}_leaf4")
    cmds.move(7, .5, -.8, r=1)
    cmds.select(f"{PFX}tree2_{itt:02}_leaf6")
    cmds.move(1.5, 1.4, 0, r=1)

    # create shader, apply, and group leaf bits
    leaf_grp = cmds.group(empty=1, n=f"{PFX}tree2_{itt:02}_leaves")
    leaf_obj_color = cmds.shadingNode('standardSurface', n=f"{PFX}tree3_{itt:02}_leaf_shd", asShader=1)
    
    # REPLACE WITH RANGE OF VALUES ONCE YOU GET HOME #
    # randomize leaf hue
    r_color = random.uniform( 0.07)
    g_color = random.uniform(.12)
    b_color = random.uniform(.18)
    cmds.setAttr(leaf_obj_color + ".baseColor",r_color, g_color, b_color)

    for i in range(15):
        leaf = f"{PFX}tree2_{itt:02}_leaf" + str(i + 1)
        cmds.parent(leaf, leaf_grp)
        cmds.select(f"{PFX}tree2_{itt:02}_leaf" + str(i + 1))
        cmds.hyperShade(assign=leaf_obj_color)

    # cleanup
    cmds.select(f"{PFX}tree2_{itt:02}_base", f"{PFX}tree2_{itt:02}_leaves")
    cmds.DeleteHistory()
    cmds.FreezeTransformations()

    curr_grp = cmds.group(n=f"{PFX}tree2_{itt:02}_GRP", empty=1)
    cmds.parent(f"{PFX}tree2_{itt:02}_leaves", f"{PFX}tree2_{itt:02}_base")
    cmds.parent(f"{PFX}tree2_{itt:02}_base", f"{PFX}tree2_{itt:02}_GRP")

    return cmds.move(0, 0, 0, curr_grp + ".scalePivot")


def mk_tree3(itt):
    # create tree base #
    cmds.polyCylinder(n=f"{PFX}tree3_{itt:02}_base1", r=.6, sx=10, sy=4)  # base 1
    # set pivot to base
    cmds.xform(piv=(0, -1, 0))
    cmds.move(0, 1, 0, r=1)
    cmds.scale(1.3, 2.3, 1.3)

    cmds.select(f"{PFX}tree3_{itt:02}_base1.f[0:9]")
    cmds.scale(1.3, .3, 1.3)

    cmds.polyExtrudeFacet(f"{PFX}tree3_{itt:02}_base1.f[41]", ls=(.8, .8, .8), t=(0, 2, -.5))
    cmds.polyExtrudeFacet(f"{PFX}tree3_{itt:02}_base1.f[41]", ls=(.8, .8, .8), t=(.5, 2, .5))
    cmds.polyExtrudeFacet(f"{PFX}tree3_{itt:02}_base1.f[41]", ls=(.8, .8, .8), t=(-1, 6, -1))

    # create branches
    cmds.polyCylinder(n=f"{PFX}tree3_{itt:02}_base2", r=.35, sx=10, sy=4)  # base 2
    cmds.move(.89, 13.25, .1)
    cmds.scale(1, 2, 1)
    cmds.rotate(19, 1.6, -29)
    cmds.duplicate(f"{PFX}tree3_{itt:02}_base2")  # base 3
    cmds.move(-1.9, -2.3, -.8, r=1)
    cmds.rotate(15, 0, -132)

    # create shader, apply, and group tree bits
    tree_grp = cmds.group(empty=1, n=f"{PFX}tree3_{itt:02}_base")
    tree_obj_color = cmds.shadingNode('standardSurface', n=f"{PFX}base_shd", asShader=1)
    cmds.setAttr(tree_obj_color + ".baseColor", 0.13, .07, .08)

    for i in range(3):
        tree = f"{PFX}tree3_{itt:02}_base" + str(i + 1)
        cmds.parent(tree, tree_grp)
        cmds.select(f"{PFX}tree3_{itt:02}_base" + str(i + 1))
        cmds.hyperShade(assign=tree_obj_color)

    # create leaves #
    cmds.polySphere(n=f"{PFX}tree3_{itt:02}_leaf1", r=1.5, sx=8, sy=8)  # leaf 1
    cmds.move(2.26, 16, .8, r=1)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf1.f[21]", f"{PFX}tree3_{itt:02}_leaf1.f[29]",
                f"{PFX}tree3_{itt:02}_leaf1.f[36]")
    cmds.move(-.7, 0, .55, r=1)
    cmds.scale(0.77, 1, 0.77)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf1.f[37:38]", f"{PFX}tree3_{itt:02}_leaf1.f[46:47]")
    cmds.move(.2, .4, -.2, r=1)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf1.f[22]", f"{PFX}tree3_{itt:02}_leaf1.f[30]")
    cmds.move(0, -.55, 0, r=1)

    # duplicate the leaf to make a block
    cmds.select(f"{PFX}tree3_{itt:02}_leaf1")
    cmds.duplicate()  # leaf 2
    cmds.move(0, -2.2, -1.8, r=1)
    cmds.rotate(0, 0, 30.4)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf2")
    cmds.duplicate()  # leaf 3
    cmds.move(-.9, 2.3, 0, r=1)
    cmds.rotate(-9.5, 10.6, -5)

    # create other blocks
    cmds.select(f"{PFX}tree3_{itt:02}_leaf1", f"{PFX}tree3_{itt:02}_leaf2", f"{PFX}tree3_{itt:02}_leaf3")
    cmds.duplicate()  # leaf 4, 5, 6
    cmds.move(-4.3, -3, -2, r=1)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf4", f"{PFX}tree3_{itt:02}_leaf5", f"{PFX}tree3_{itt:02}_leaf6")
    cmds.duplicate()  # leaf 7, 8, 9
    cmds.move(2.3, 2.1, 0, r=1)
    cmds.rotate(12, 45, 0, r=1)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf7", f"{PFX}tree3_{itt:02}_leaf8", f"{PFX}tree3_{itt:02}_leaf9")
    cmds.duplicate()  # leaf 10, 11, 12
    cmds.move(0, 3.8, 0, r=1)
    cmds.rotate(12, 45, 30, r=1)

    # refine leaf positions
    cmds.select(f"{PFX}tree3_{itt:02}_leaf12")
    cmds.move(-2.4, -3.6, 1.85, r=1)
    cmds.rotate(0, 0, -83.9, r=1)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf10")
    cmds.move(-1.4, -2.1, -1.3, r=1)
    cmds.rotate(-186.8, 0, 0, r=1)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf11")
    cmds.move(-.64, 1.2, 2.79, r=1)
    cmds.rotate(-121.8, 0, 0, r=1)
    cmds.select(f"{PFX}tree3_{itt:02}_leaf9")
    cmds.move(2.1, 3.1, 3.94, r=1)
    cmds.rotate(137.7, -14.4, -11.8, r=1)

    # create shader, apply, and group leaf bits
    leaf_grp = cmds.group(empty=1, n=f"{PFX}tree3_{itt:02}_leaves")
    leaf_obj_color = cmds.shadingNode('standardSurface', n=f"{PFX}tree3_{itt:02}_leaf_shd", asShader=1)
    
    # REPLACE WITH RANGE OF VALUES ONCE YOU GET HOME #
    # randomize leaf hue
    r_color = random.uniform( 0.08)
    g_color = random.uniform(.16)
    b_color = random.uniform(.07)
    cmds.setAttr(leaf_obj_color + ".baseColor",r_color, g_color, b_color)

    for i in range(12):
        leaf = f"{PFX}tree3_{itt:02}_leaf" + str(i + 1)
        cmds.parent(leaf, leaf_grp)
        cmds.select(f"{PFX}tree3_{itt:02}_leaf" + str(i + 1))
        cmds.hyperShade(assign=leaf_obj_color)

    # cleanup
    cmds.select(f"{PFX}tree3_{itt:02}_base", f"{PFX}tree3_{itt:02}_leaves")
    cmds.DeleteHistory()
    cmds.FreezeTransformations()

    curr_grp = cmds.group(n=f"{PFX}tree3_{itt:02}_GRP", empty=1)
    cmds.parent(f"{PFX}tree3_{itt:02}_leaves", f"{PFX}tree3_{itt:02}_base")
    cmds.parent(f"{PFX}tree3_{itt:02}_base", f"{PFX}tree3_{itt:02}_GRP")

    return cmds.move(0, 0, 0, curr_grp + ".scalePivot")


def lights():
    # create sky
    skydome = cmds.shadingNode('aiSkyDomeLight', asLight=True)
    physical_sky_shader = cmds.createNode('aiPhysicalSky')
    cmds.connectAttr(physical_sky_shader + ".outColor", skydome + ".color")
    cmds.setAttr(skydome + ".intensity", .7)
    cmds.rename(skydome, f"{PFX}physicalSky")

    # create lights
    cmds.directionalLight(n=f"{PFX}dirLight1")  # light 1
    cmds.rotate(-38, 0, 0)
    cmds.setAttr(f"{PFX}dirLight1.color", .2, .3, .4)
    cmds.setAttr(f"{PFX}dirLight1.intensity", .7)

    cmds.directionalLight(n=f"{PFX}dirLight2")  # light 2
    cmds.rotate(-38, 180, 0)
    cmds.setAttr(f"{PFX}dirLight1.color", .5, .3, .3)
    cmds.setAttr(f"{PFX}dirLight1.intensity", .5)

    return cmds.group(f"{PFX}physicalSky", f"{PFX}dirLight1", f"{PFX}dirLight2", n=f"{PFX}lights")


def rand_tree(itt):
    all_trees = [mk_tree1, mk_tree2, mk_tree3]
    selected_tree = random.choice(all_trees)

    return selected_tree(itt)


if __name__ == "__main__":
    if cmds.objExists(PFX + "*"):
        cmds.delete(PFX + "*")

    verts = cmds.ls(sl=1, fl=1)

    for i, vert in enumerate(verts, start=1):
        # uniform random scale and rotate
        rand_scale = random.uniform(.7, 1.2)
        rand_rotation = random.randint(0, 360)

        # set seed
        # random.seed = 10

        # select a random tree
        curr = rand_tree(i)

        # move to selected position and randomly scale and rotate
        xpos, ypos, zpos = cmds.pointPosition(vert)
        cmds.move(xpos, ypos, zpos)
        cmds.scale(rand_scale, rand_scale, rand_scale)
        cmds.rotate(0, rand_rotation, 0)

    cmds.group(PFX + "tree?_*_GRP", n=PFX + "forest")
    cmds.select(cl=1)

    lights()

    print("Done!")
